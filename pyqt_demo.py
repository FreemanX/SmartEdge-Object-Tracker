import sys

import numpy as np
import queue
import typing
import json
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QDialog

import pyqt_demo_ui as UI

from cloud.upload import *
from inference_backend import *
from libs.utils import *
from libs.Log import Log

from ui.new_trip import NewTripDialog
from ui.upload_trip import UploadTripDialog


class BufferPackedResult:
    def __init__(self, buffer_size=2):
        self.buffer = queue.Queue(buffer_size)

    def put(self, packed_result: dict):
        try:
            self.buffer.put_nowait(packed_result)
        except queue.Full:
            self.buffer.get_nowait()
            self.buffer.put_nowait(packed_result)

    def get(self) -> typing.Tuple[bool, dict]:
        try:
            packed_result = self.buffer.get_nowait()
            self.buffer.task_done()
            return True, packed_result
        except queue.Empty:
            return False, {}


class DetectorApp(UI.Ui_MainWindow, BufferPackedResult):
    def __init__(self, video_file: None):
        BufferPackedResult.__init__(self)
        self.qt_app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        # fix the GUI window
        self.MainWindow.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.MainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.MainWindow.setWindowFlag(Qt.WindowMinimizeButtonHint, False)

        self.capture_a_frame = False
        self.inference_backend = InferenceBackend()
        self.current_temperature = get_initial_temperature()
        self.fpe = FrameProcessingEngine(self.inference_backend, self, video_file)
        self.metadata = {}
        self.start_trip_time = ''
        self.trip_root_dir = 'trips'
        self.trip_name = 'trip'

        self.set_ui_init_values()
        self.set_ui_init_behaviour()
        self.set_ui_actions()

    def set_ui_init_values(self):
        self.inference_backend.set_confidence(0.5)
        self.update_sensitivity_label()
        self.update_start_button()

    def set_ui_init_behaviour(self):
        # self.pushButton_start.setEnabled(False)
        # self.pushButton_capture.setEnabled(False)
        self.horizontalScrollBar_sensitivity.setEnabled(False)

    def set_ui_actions(self):
        # ---------  Sample Action
        self.MainWindow.closeEvent = self.ask_stop_app
        self.pushButton_exit.clicked.connect(lambda: self.MainWindow.close())
        # ---------  Sample Action end

        self.fpe.sig_source.connect(self.update_pp_to_ui)
        self.horizontalScrollBar_sensitivity.valueChanged.connect(self.on_sensitivity_change)
        self.pushButton_start.clicked.connect(self.on_start_clicked)
        self.pushButton_capture.clicked.connect(self.on_capture_clicked)
        self.pushButton_new_trip.clicked.connect(self.on_new_trip_clicked)
        self.pushButton_upload.clicked.connect(self.on_upload_clicked)

    def on_capture_clicked(self):
        self.pushButton_capture.setText("Capturing")
        self.pushButton_capture.setEnabled(False)
        # TODO
        self.capture_a_frame = True

    def on_start_clicked(self):
        self.save_metadata()
        self.fpe.start_detection = not self.fpe.start_detection
        self.update_start_button()
        self.pushButton_new_trip.setEnabled(not self.fpe.start_detection)
        self.pushButton_upload.setEnabled(not self.fpe.start_detection)
        self.horizontalScrollBar_sensitivity.setEnabled(self.fpe.start_detection)
        self.pushButton_start.setEnabled(self.fpe.start_detection)
        self.pushButton_capture.setEnabled(self.fpe.start_detection)

    def update_start_button(self):
        if self.fpe.start_detection:
            self.pushButton_start.setText("Stop")
        else:
            self.pushButton_start.setText("Start")

    def on_new_trip_clicked(self):
        self.newTripDialog = NewTripDialog()
        result = self.newTripDialog.exec()
        if result == QDialog.Accepted:
            self.metadata = {}
            self.metadata['latitude'] = self.newTripDialog.ui.lineEdit_latitude.text()
            self.metadata['longitude'] = self.newTripDialog.ui.lineEdit_longitude.text()
            self.start_trip_time = datetime.now().strftime("%Y%m%d%H%M%S")
            self.trip_root_dir = 'trips'
            self.trip_name = 'trip'
            self.trip_dir = "%s/%s_%s" % (self.trip_root_dir, self.trip_name, self.start_trip_time)
            create_dir_if_not_exists(self.trip_dir)

            self.horizontalScrollBar_sensitivity.setEnabled(True)
            self.pushButton_start.setEnabled(True)
            self.pushButton_capture.setEnabled(True)

    def on_upload_clicked(self):
        self.uploadTripDialog = UploadTripDialog()
        result = self.uploadTripDialog.exec()
        if result == QDialog.Accepted:
            pass

    def on_sensitivity_change(self):
        conf_val = (100 - self.horizontalScrollBar_sensitivity.value()) / 100
        self.inference_backend.set_confidence(conf_val)
        self.update_sensitivity_label()

    def update_sensitivity_label(self):
        scroll_bar_value = round(
            100 * (1 - self.inference_backend.get_confidence()))
        self.horizontalScrollBar_sensitivity.setValue(int(scroll_bar_value))
        self.label_sensitivity.setText(f"{scroll_bar_value}")

    def update_pp_to_ui(self, img):  # update processed frame to ui
        self.label_camview.setPixmap(QPixmap.fromImage(img))
        self.process_results()

    def save_metadata(self):
        try:
            if self.fpe.start_detection:
                json_filename = "meta_%s_%s_%s_%s.json" % (
                    self.trip_name, self.start_trip_time, self.metadata['latitude'], self.metadata['longitude'])
                with open("%s/%s" % (self.trip_dir, json_filename), "w") as outfile:
                    json.dump(self.metadata, outfile)
                self.metadata = {}
                self.label_camview.clear()
                self.statusbar.showMessage('')
                self.label_camview.setText('Camera View')
        except Exception as e:
            Log.error(f"Saving metadata error: {e}")

    def process_results(self):
        """
        Further result processing procedure goes here.
        """
        ret, results = self.fpe.get()
        if not ret:
            return
        # Example: show info on status bar.
        pad_size = 35
        msg_str = f"FPS: {results['fps']} ".ljust(pad_size)
        msg_str += f"Inference Time: {round(results['inference_time'] * 1000, 2)}ms ".ljust(pad_size)
        msg_str += f"Num COTS: {round(results['n_objects'])} ".ljust(pad_size)
        msg_str += f"End-to-end time: {round(results['total_time'] * 1000, 2)}ms".ljust(pad_size)
        self.statusbar.showMessage(msg_str)

        # ---------- Displaying COTS -----------
        cots_patch = np.zeros((140, 1260, 3), dtype=np.uint8)
        # boxes = sorted(results['boxes'][:36], key=lambda b: b[0])
        # p_size = 140 if len(boxes) < 10 else 70
        boxes = sorted(results['boxes'][:9], key=lambda b: b[1], reverse=True)
        boxes = sorted(boxes, key=lambda b: b[0])
        p_size = 140 if len(boxes) < 10 else 70
        for idx, box in enumerate(boxes):
            kp = [int(x) for x in box]
            patch = results['raw_frame'][kp[1]:kp[3], kp[0]:kp[2]]#.copy()
            patch = cv.resize(patch, (p_size, p_size))
            x_pos = idx * p_size if p_size == 140 else (idx % 18) * p_size
            y_pox = 0 if p_size == 140 else idx // 18 * p_size
            cots_patch[y_pox:y_pox+p_size, x_pos:x_pos+p_size, :] = patch[:, :, :]

        patch_qt = QPixmap.fromImage(cvt_cv_to_qt(cots_patch, 1260, 140))
        self.label_cots.setPixmap(patch_qt)


        # ---------- Handle image saving -----------
        # save processed frame
        currentTime = str(round(10 * time.time()))
        file_prefix = f"{self.trip_name}_{self.start_trip_time}_{currentTime}"
        saveSensorData = False
        if self.fpe.start_detection and results['n_objects'] > 0:
            saveSensorData = True
            cv.imwrite(
                f"{self.trip_dir}/{file_prefix}_processed.jpg",
                results['out_frame']
            )
            # save raw frame
            cv.imwrite(
                f"{self.trip_dir}/{file_prefix}.jpg",
                results['raw_frame']
            )
            # save labels
            with open(f'{self.trip_dir}/{file_prefix}.txt', 'w') as f:
                for label in convert_bbox_to_labels(results['boxes'], results['raw_frame']):
                    f.write(f"0 {label}\n")

        if self.fpe.start_detection and self.capture_a_frame:
            saveSensorData = True
            cv.imwrite(
                f"{self.trip_dir}/{file_prefix}_captured.jpg",
                results['raw_frame']
            )
            self.capture_a_frame = False
            self.pushButton_capture.setEnabled(True)
            self.pushButton_capture.setText("Capture")
        # ---------- End Handle image saving -----------

        # Save sensor data into metadata
        if saveSensorData:
            self.metadata[currentTime] = {}
            self.metadata[currentTime]['temperature'] = round(
                self.current_temperature, 1)

        self.put(results)

    def ask_stop_app(self, event):
        # TODO: Skip ask if haven't started new trip
        # TODO: QMessageBox button size
        msg = QMessageBox()
        msg.setWindowTitle("Exit?")
        msg.setText("Confirm exit this application?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setIcon(QMessageBox.Warning)
        ret = msg.exec_()
        if ret == QMessageBox.Ok:
            Log.info("Program exit.")
            self.qt_app.closeAllWindows()
            event.accept()
        else:
            event.ignore()

    def exit_procedure(self):
        self.save_metadata()
        Log.info(f"Exiting procedure in prrogress...")
        self.inference_backend.release_resrouce()
        self.fpe.thread_run = False
        self.fpe.exit(0)
        time.sleep(3)
        Log.info(f"Exiting procedure done.")

    def launch(self):
        self.MainWindow.show()
        self.fpe.start()
        _exit_code = self.qt_app.exec_()
        self.exit_procedure()
        return _exit_code


class FrameProcessingEngine(QThread, BufferPackedResult):
    sig_source = pyqtSignal(QImage)

    def __init__(self, inference_backend: InferenceBackend, detector: DetectorApp, vid_file: None):
        QThread.__init__(self)
        BufferPackedResult.__init__(self)
        self.thread_run = True
        self.vid_mode = False
        self.vid_file = vid_file
        if not vid_file:  # see if we want demo on a video file
            self.cap = cv.VideoCapture(gstreamer_pipeline())
        else:
            self.cap = cv.VideoCapture(vid_file)
            if not self.cap.isOpened():
                Log.error(f"Failed to open video file {vid_file}!")
                raise Exception(f"Failed to open video file {vid_file}!")
            self.vid_mode = True
        self.frame_width = self.cap.get(cv.CAP_PROP_FRAME_WIDTH)
        self.frame_height = self.cap.get(cv.CAP_PROP_FRAME_HEIGHT)

        self.inf_bkend = inference_backend
        # self.start_detection = False
        # TODO: DEBUG only reset once done -- Freeman
        self.start_detection = True
        self.detector = detector

    def run(self):  # Implement QThread function
        while self.thread_run:
            timer = time.time()
            ret, frame = self.cap.read()
            if self.vid_mode and not self.start_detection:
                time.sleep(0.043333)
            if not ret and self.vid_mode:
                Log.info(f"End of video reached, reset to the first frame.")
                self.cap.release()
                self.cap = cv.VideoCapture(self.vid_file)
            elif not ret:
                Log.warning(
                    "Failed to get video frame from camera. Retrying...")
                continue
            if frame is None:
                continue
            raw_frame = frame.copy()
            if self.start_detection:
                results = self.inf_bkend.inference(frame)
                results['n_objects'] = 0 # TODO: Debug only, reset once done -- Freeman
            else:
                results = {
                    'out_frame': frame,
                    'inference_time': 0,
                    'n_objects': 0,
                    'boxes': []
                }
            # copy an instance for display
            out_frame = results['out_frame'].copy()
            results['raw_frame'] = raw_frame
            results['total_time'] = time.time() - timer
            try:
                results['fps'] = round(
                    1/results['inference_time']) if self.start_detection else 0
            except ZeroDivisionError:  # just be safe
                results['fps'] = 0
            self.put(results)
            # ; separated text, ; is line separator.
            if self.start_detection:
                self.detector.current_temperature = get_next_temperature(
                    self.detector.current_temperature)
                frame_text = f"COTS: {results['n_objects']}; FPS: {results['fps']}; Temperature: {round(self.detector.current_temperature, 1)}"
                out_frame = add_text_to_frame(out_frame, frame_text)
            self.sig_source.emit(cvt_cv_to_qt(out_frame))

        self.cap.release()


if __name__ == '__main__':
    video_file = sys.argv[1] if len(sys.argv) > 1 else None
    app = DetectorApp(video_file)
    exit_code = app.launch()
    Log.info(f"Exit code: {exit_code}")
    sys.exit(exit_code)
