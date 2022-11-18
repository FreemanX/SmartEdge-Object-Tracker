import os
import random
import time
import pathlib

import cv2
import numpy as np
import ctypes
import pycuda.autoinit
import pycuda.driver as cuda
import tensorrt as trt


from libs.Log import Log
from libs.sort import Sort

COLOR_PALETTE = [
    (230, 25, 75),
    (60, 180, 75),
    (67, 99, 216),
    (245, 130, 49),
    (145, 30, 37),
    (22, 246, 12),
    (0, 128, 128),
    (154, 99, 36),
    (128, 0, 0),
    (128, 128, 0),
    (0, 0, 117),
    (128, 128, 128),
    (0, 0, 0),
    (0, 0, 255)
]

class InferenceBackend():
    categories = ["COTS"]

    def __init__(self) -> None:
        PLUGIN_LIBRARY, engine_file_path = gen_engine_model()
        ctypes.CDLL(PLUGIN_LIBRARY)
        self.yolov5_wrapper = Yolov5TRT(engine_file_path, self.categories)

    def reset_object_count(self):
        self.yolov5_wrapper.reset_tracker()

    def set_confidence(self, conf: float):
        self.yolov5_wrapper.set_conf_thresh(conf)

    def get_confidence(self):
        return self.yolov5_wrapper.conf_thresh

    def set_enable_tracker(self, v:bool):
        self.yolov5_wrapper.enable_tracker = v
    
    def get_enable_tracker(self):
        return self.yolov5_wrapper.enable_tracker

    def release_resrouce(self):
        """
        Must call this function on exit
        """
        self.yolov5_wrapper.destroy()
    
    def inference(self, input_frame):
        output_frame, inference_time, n_objects, \
                bbox_lst, conf_lst, cls_lst, \
                cots_cnt, track_dict = self.yolov5_wrapper.inference(input_frame)
        return {
            'out_frame': output_frame,
            'inference_time': inference_time,
            'n_objects': n_objects,
            'boxes': bbox_lst,
            'confs': conf_lst,
            'cls_lst': cls_lst,
            'cots_cnt': cots_cnt,
            'track_dict': track_dict
        }


def convert_bbox_to_labels(bbox_lst, frame):
    labels = []
    h, w, _ = frame.shape
    for kp in bbox_lst:
        kw = kp[2] - kp[0]
        kh = kp[3] - kp[1]
        x = kp[0] + kw / 2
        y = kp[1] + kh / 2
        labels.append(f"{x / w} {y / h} {kw / w} {kh / h}")
    return labels


def gen_engine_model():
    machine_id = ''
    with open('/etc/machine-id', 'r') as f:
        machine_id = f.readline().strip()
    assert len(machine_id) > 0
    trt_path = './trt'
    trt_so = f'{trt_path}/build/libmyplugins.so'
    trt_yolov5 = f'{trt_path}/build/yolov5'

    Log.info("Checking plugin lib...")
    Log.info(f"Building necessary library...")
    pathlib.Path(f'{trt_path}/build').mkdir(parents=True, exist_ok=True)
    cwd = os.getcwd()
    os.chdir(f'{trt_path}/build')
    os.system('cmake ..')
    os.system('make')
    os.chdir(cwd)
    Log.info('[OK] Plugin files has been built.')

    engine_file = f'./weights/{machine_id}.engine'
    Log.info(f"Checking model file({engine_file})...")
    if not pathlib.Path(engine_file).is_file():
        Log.info(f"Building TensorRT model, this may take a while, please wait...")
        os.system(
            f"{trt_yolov5} -s weights/yolov5n_720_cots_best.wts {engine_file} n")
    else:
        Log.info('[OK] model file ready.')

    return trt_so, engine_file


def plot_one_box(x, img, color=None, label=None, line_thickness=None):
    """
    description: Plots one bounding box on image img,
                 this function comes from YoLov5 project.
    param:
        x:      a box likes [x1,y1,x2,y2]
        img:    an opencv image object
        color:  color to draw rectangle, such as (0,255,0)
        label:  str
        line_thickness: int
    return:
        no return

    """
    # line/font thickness
    tl = (line_thickness or round(
        0.002 * (img.shape[0] + img.shape[1]) / 2) + 1)
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(
            img,
            label,
            (c1[0], c1[1] - 2),
            0,
            tl / 3,
            [225, 255, 255],
            thickness=tf,
            lineType=cv2.LINE_AA,
        )

def draw_boxes(
    img, bbox, identities=None, categories=None, names=None, offset=(0, 0), colors=[]
):
    object_dict = {}
    """Function to Draw Bounding boxes"""
    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(i) for i in box]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]
        cat = int(categories[i]) if categories is not None else 0
        id = int(identities[i]) if identities is not None else 0
        object_dict[id] = [x1, y1, x2, y2]
        color = colors[id % len(colors)]
        label = str(id) + ":" + names[cat]
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(img, (x1, y1 - 20), (x1 + w, y1), color, -1)
        cv2.putText(
            img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 255], 1
        )
        # cv2.circle(img, data, 6, color,-1)
    return img, object_dict

class Yolov5TRT(object):
    """
    description: A YOLOv5 class that warps TensorRT ops, preprocess and postprocess ops.
    """

    def __init__(self, engine_file_path, categories: list):
        # Create a Context on this device,
        self.ctx = cuda.Device(0).make_context()
        stream = cuda.Stream()
        trt_logger = trt.Logger(trt.Logger.INFO)
        runtime = trt.Runtime(trt_logger)
        self.categories = categories
        self.conf_thresh = 0.5

        self.enable_tracker = False
        self.reset_tracker()

        # Deserialize the engine from file
        with open(engine_file_path, "rb") as f:
            engine = runtime.deserialize_cuda_engine(f.read())
        context = engine.create_execution_context()

        host_inputs = []
        cuda_inputs = []
        host_outputs = []
        cuda_outputs = []
        bindings = []

        for binding in engine:
            size = trt.volume(engine.get_binding_shape(
                binding)) * engine.max_batch_size
            dtype = trt.nptype(engine.get_binding_dtype(binding))
            # Allocate host and device buffers
            host_mem = cuda.pagelocked_empty(size, dtype)
            cuda_mem = cuda.mem_alloc(host_mem.nbytes)
            # Append the device buffer to device bindings.
            bindings.append(int(cuda_mem))
            # Append to the appropriate list.
            if engine.binding_is_input(binding):
                self.input_w = engine.get_binding_shape(binding)[-1]
                self.input_h = engine.get_binding_shape(binding)[-2]
                host_inputs.append(host_mem)
                cuda_inputs.append(cuda_mem)
            else:
                host_outputs.append(host_mem)
                cuda_outputs.append(cuda_mem)

        # Store
        self.stream = stream
        self.context = context
        self.engine = engine
        self.host_inputs = host_inputs
        self.cuda_inputs = cuda_inputs
        self.host_outputs = host_outputs
        self.cuda_outputs = cuda_outputs
        self.bindings = bindings
        self.batch_size = engine.max_batch_size

    def reset_tracker(self):
        self.sort_tracker = Sort(max_age=1, min_hits=2, iou_threshold=0.05)
        self.cots_cnt = 0
        self.cots_id_cnt_dict = {}

    def set_conf_thresh(self, v):
        self.conf_thresh = v

    def inference(self, raw_image):
        # Make self the active context, pushing it on top of the context stack.
        self.ctx.push()
        # Restore
        stream = self.stream
        context = self.context
        host_inputs = self.host_inputs
        cuda_inputs = self.cuda_inputs
        host_outputs = self.host_outputs
        cuda_outputs = self.cuda_outputs
        bindings = self.bindings
        # Do image preprocess
        batch_image_raw = []
        batch_origin_h = []
        batch_origin_w = []
        batch_input_image = np.empty(
            shape=[self.batch_size, 3, self.input_h, self.input_w])
        input_image, image_raw, origin_h, origin_w = self.preprocess_image(
            raw_image)
        batch_image_raw.append(raw_image)
        batch_origin_h.append(origin_h)
        batch_origin_w.append(origin_w)
        np.copyto(batch_input_image[0], input_image)
        batch_input_image = np.ascontiguousarray(batch_input_image)

        # Copy input image to host buffer
        np.copyto(host_inputs[0], batch_input_image.ravel())
        start = time.time()
        # Transfer input data  to the GPU.
        cuda.memcpy_htod_async(cuda_inputs[0], host_inputs[0], stream)
        # Run inference.
        context.execute_async(
            batch_size=self.batch_size, bindings=bindings, stream_handle=stream.handle
        )
        # Transfer predictions back from the GPU.
        cuda.memcpy_dtoh_async(host_outputs[0], cuda_outputs[0], stream)
        # Synchronize the stream
        # noinspection PyArgumentList
        stream.synchronize()
        # end = time.time()
        # Remove any context from the top of the context stack, deactivating it.
        self.ctx.pop()
        # Here we use the first row of output in that batch_size = 1
        output = host_outputs[0]
        # Do postprocess
        result_boxes = []
        for i in range(self.batch_size):
            result_boxes, result_scores, result_classid = self.post_process(
                output[i * 6001: (i + 1) * 6001], batch_origin_h[i], batch_origin_w[i]
            )
            # Draw rectangles and labels on the original image
            if not self.enable_tracker:
                for j in range(len(result_boxes)):
                    box = result_boxes[j]
                    plot_one_box(
                        box,
                        batch_image_raw[i],
                        label="{}:{:.2f}".format(
                            self.categories[int(result_classid[j])], 
                            result_scores[j]
                        ),
                        line_thickness=2,
                        color=(0, 0, 255)
                    )
        track_dict = {}
        if self.enable_tracker:
            dets_to_sort = np.empty((0, 6))
            for j in range(len(result_boxes)):
                box = result_boxes[j]
                conf = result_scores[j]
                cls_id = round(result_classid[j])
                dets_to_sort = np.vstack(
                    (dets_to_sort, np.array([box[0], box[1], box[2], box[3], \
                        conf, cls_id]))
                )
            tracked_dets = self.sort_tracker.update(dets_to_sort)
            if len(tracked_dets) > 0:
                bbox_xyxy = tracked_dets[:, :4]
                identities = tracked_dets[:, 8]

                counter_id = [0.] * len(identities)
                for k in range(len(identities)):
                    tid = identities[k]
                    if tid not in self.cots_id_cnt_dict:
                        self.cots_id_cnt_dict[tid] = len(self.cots_id_cnt_dict) + 1
                    counter_id[k] = self.cots_id_cnt_dict[tid]

                categories = tracked_dets[:, 4]
                _, track_dict = draw_boxes(
                    batch_image_raw[0],
                    bbox_xyxy,
                    counter_id,
                    categories,
                    self.categories,
                    colors=COLOR_PALETTE,
                )
                self.cots_cnt = len(self.cots_id_cnt_dict)
        end = time.time()
        return batch_image_raw[0], \
            end - start, len(result_boxes), \
            result_boxes, \
            result_scores, \
            result_classid, \
            self.cots_cnt, \
            track_dict

    def destroy(self):
        try:
            # Remove any context from the top of the context stack, deactivating it.
            self.ctx.pop()
            Log.info("CUDA Context popped.")
        except Exception as e:
            Log.warning(f"Destroying cuda ctx exception: {e}")
        finally:
            Log.info("Yolov5 TRT Backend Destroyed")

    def preprocess_image(self, raw_bgr_image):
        """
        description: Convert BGR image to RGB,
                     resize and pad it to target size, normalize to [0,1],
                     transform to NCHW format.
        param:
            input_image_path: str, image path
        return:
            image:  the processed image
            image_raw: the original image
            h: original height
            w: original width
        """
        image_raw = raw_bgr_image
        h, w, c = image_raw.shape
        image = cv2.cvtColor(image_raw, cv2.COLOR_BGR2RGB)
        # Calculate width and height and paddings
        r_w = self.input_w / w
        r_h = self.input_h / h
        if r_h > r_w:
            tw = self.input_w
            th = int(r_w * h)
            tx1 = tx2 = 0
            ty1 = int((self.input_h - th) / 2)
            ty2 = self.input_h - th - ty1
        else:
            tw = int(r_h * w)
            th = self.input_h
            tx1 = int((self.input_w - tw) / 2)
            tx2 = self.input_w - tw - tx1
            ty1 = ty2 = 0
        # Resize the image with long side while maintaining ratio
        image = cv2.resize(image, (tw, th))
        # Pad the short side with (128,128,128)
        image = cv2.copyMakeBorder(
            image, ty1, ty2, tx1, tx2, cv2.BORDER_CONSTANT, (128, 128, 128)
        )
        image = image.astype(np.float32)
        # Normalize to [0,1]
        image /= 255.0
        # HWC to CHW format:
        image = np.transpose(image, [2, 0, 1])
        # CHW to NCHW format
        image = np.expand_dims(image, axis=0)
        # Convert the image to row-major order, also known as "C order":
        image = np.ascontiguousarray(image)
        return image, image_raw, h, w

    def xywh2xyxy(self, origin_h, origin_w, x):
        """
        description:    Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
        param:
            origin_h:   height of original image
            origin_w:   width of original image
            x:          A boxes numpy, each row is a box [center_x, center_y, w, h]
        return:
            y:          A boxes numpy, each row is a box [x1, y1, x2, y2]
        """
        y = np.zeros_like(x)
        r_w = self.input_w / origin_w
        r_h = self.input_h / origin_h
        if r_h > r_w:
            y[:, 0] = x[:, 0] - x[:, 2] / 2
            y[:, 2] = x[:, 0] + x[:, 2] / 2
            y[:, 1] = x[:, 1] - x[:, 3] / 2 - \
                (self.input_h - r_w * origin_h) / 2
            y[:, 3] = x[:, 1] + x[:, 3] / 2 - \
                (self.input_h - r_w * origin_h) / 2
            y /= r_w
        else:
            y[:, 0] = x[:, 0] - x[:, 2] / 2 - \
                (self.input_w - r_h * origin_w) / 2
            y[:, 2] = x[:, 0] + x[:, 2] / 2 - \
                (self.input_w - r_h * origin_w) / 2
            y[:, 1] = x[:, 1] - x[:, 3] / 2
            y[:, 3] = x[:, 1] + x[:, 3] / 2
            y /= r_h

        return y

    def post_process(self, output, origin_h, origin_w):
        """
        description: postprocess the prediction
        param:
            output:     A numpy likes [num_boxes,cx,cy,w,h,conf,cls_id, cx,cy,w,h,conf,cls_id, ...]
            origin_h:   height of original image
            origin_w:   width of original image
        return:
            result_boxes: finally boxes, a boxes numpy, each row is a box [x1, y1, x2, y2]
            result_scores: finally scores, a numpy, each element is the score corresponding to box
            result_classid: finally classid, a numpy, each element is the classid corresponding to box
        """
        # Get the num of boxes detected
        num = int(output[0])
        # Reshape to a two-dimensional ndarray
        pred = np.reshape(output[1:], (-1, 6))[:num, :]
        # Do nms
        boxes = self.non_max_suppression(
            pred, origin_h, origin_w, conf_thres=self.conf_thresh, nms_thres=.3)
        result_boxes = boxes[:, :4] if len(boxes) else np.array([])
        result_scores = boxes[:, 4] if len(boxes) else np.array([])
        result_classid = boxes[:, 5] if len(boxes) else np.array([])
        return result_boxes, result_scores, result_classid

    @staticmethod
    def bbox_iou(box1, box2, x1y1x2y2=True):
        """
        description: compute the IoU of two bounding boxes
        param:
            box1: A box coordinate (can be (x1, y1, x2, y2) or (x, y, w, h))
            box2: A box coordinate (can be (x1, y1, x2, y2) or (x, y, w, h))
            x1y1x2y2: select the coordinate format
        return:
            iou: computed iou
        """
        if not x1y1x2y2:
            # Transform from center and width to exact coordinates
            b1_x1, b1_x2 = box1[:, 0] - box1[:, 2] / \
                2, box1[:, 0] + box1[:, 2] / 2
            b1_y1, b1_y2 = box1[:, 1] - box1[:, 3] / \
                2, box1[:, 1] + box1[:, 3] / 2
            b2_x1, b2_x2 = box2[:, 0] - box2[:, 2] / \
                2, box2[:, 0] + box2[:, 2] / 2
            b2_y1, b2_y2 = box2[:, 1] - box2[:, 3] / \
                2, box2[:, 1] + box2[:, 3] / 2
        else:
            # Get the coordinates of bounding boxes
            b1_x1, b1_y1, b1_x2, b1_y2 = \
                box1[:, 0], box1[:, 1], box1[:, 2], box1[:, 3]
            b2_x1, b2_y1, b2_x2, b2_y2 = \
                box2[:, 0], box2[:, 1], box2[:, 2], box2[:, 3]

        # Get the coordinates of the intersection rectangle
        inter_rect_x1 = np.maximum(b1_x1, b2_x1)
        inter_rect_y1 = np.maximum(b1_y1, b2_y1)
        inter_rect_x2 = np.minimum(b1_x2, b2_x2)
        inter_rect_y2 = np.minimum(b1_y2, b2_y2)
        # Intersection area
        inter_area = np.clip(inter_rect_x2 - inter_rect_x1 + 1, 0, None) * np.clip(
            inter_rect_y2 - inter_rect_y1 + 1, 0, None
        )
        # Union Area
        b1_area = (b1_x2 - b1_x1 + 1) * (b1_y2 - b1_y1 + 1)
        b2_area = (b2_x2 - b2_x1 + 1) * (b2_y2 - b2_y1 + 1)

        iou = inter_area / (b1_area + b2_area - inter_area + 1e-16)

        return iou

    def non_max_suppression(self, prediction, origin_h, origin_w, conf_thres, nms_thres=0.4):
        """
        description: Removes detections with lower object confidence score than 'conf_thres' and performs
        Non-Maximum Suppression to further filter detections.
        param:
            prediction: detections, (x1, y1, x2, y2, conf, cls_id)
            origin_h: original image height
            origin_w: original image width
            conf_thres: a confidence threshold to filter detections
            nms_thres: an iou threshold to filter detections
        return:
            boxes: output after nms with the shape (x1, y1, x2, y2, conf, cls_id)
        """
        # Get the boxes that score > CONF_THRESH
        boxes = prediction[prediction[:, 4] >= conf_thres]
        # Transform bbox from [center_x, center_y, w, h] to [x1, y1, x2, y2]
        boxes[:, :4] = self.xywh2xyxy(origin_h, origin_w, boxes[:, :4])
        # clip the coordinates
        boxes[:, 0] = np.clip(boxes[:, 0], 0, origin_w - 1)
        boxes[:, 2] = np.clip(boxes[:, 2], 0, origin_w - 1)
        boxes[:, 1] = np.clip(boxes[:, 1], 0, origin_h - 1)
        boxes[:, 3] = np.clip(boxes[:, 3], 0, origin_h - 1)
        # Object confidence
        confs = boxes[:, 4]
        # Sort by the confs
        boxes = boxes[np.argsort(-confs)]
        # Perform non-maximum suppression
        keep_boxes = []
        while boxes.shape[0]:
            large_overlap = (self.bbox_iou(np.expand_dims(
                boxes[0, :4], 0), boxes[:, :4]) > nms_thres)
            label_match = boxes[0, -1] == boxes[:, -1]
            # Indices of boxes with lower confidence scores, large IOUs and matching labels
            invalid = large_overlap & label_match
            keep_boxes += [boxes[0]]
            boxes = boxes[~invalid]
        boxes = np.stack(keep_boxes, 0) if len(keep_boxes) else np.array([])
        return boxes