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

import ui.app_ui as UI

from cloud.upload import *
from inference_backend import *
from libs.utils import *
from libs.Log import Log
from sensor.SensorManager import SensorManager

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
        self.sensor_manager = SensorManager()
        self.log_started = False
        try:  # if camera is working or video files can be loaded
            self.fpe = FrameProcessingEngine(self.inference_backend, self.sensor_manager, video_file)
            self.sensor_manager.thread_start()
            self.track_id_patch_dict = {}
            self.metadata = {}
            self.start_trip_time = ''
            self.trip_root_dir = 'trips'
            self.trip_name = 'trip'

            self.set_ui_actions()
            self.set_ui_init_values()
        except Exception as e:
            Log.warning(e)
            self.fpe = None
            self.widget_error_screen.setVisible(True)
            Log.error(e)
        self.exit_code = 0
        self.pushButton_exit.clicked.connect(lambda: self.MainWindow.close())

    def set_ui_init_values(self):
        self.widget_error_screen.setVisible(False)
        self.inference_backend.set_confidence_thresh(0.4)
        self.update_sensitivity_label()
        self.update_start_button()
        self.pushButton_start.setEnabled(False)
        self.pushButton_capture.setEnabled(False)

        self.pushButton_object_track.setChecked(True)
        self.pushButton_object_track.setText("Tracking COTS")
        self.pushButton_show_anno.setChecked(True)
        self.pushButton_show_anno.setText("Showing Annotation")

    def set_ui_actions(self):
        # ---------  Sample Action
        self.MainWindow.closeEvent = self.ask_stop_app
        # ---------  Sample Action end

        self.fpe.sig_source.connect(self.update_pp_to_ui)
        self.horizontalScrollBar_sensitivity.valueChanged.connect(self.on_sensitivity_change)
        self.pushButton_start.clicked.connect(self.on_start_clicked)
        self.pushButton_capture.clicked.connect(self.on_capture_clicked)
        self.pushButton_new_trip.clicked.connect(self.on_new_trip_clicked)
        self.pushButton_upload.clicked.connect(self.on_upload_clicked)
        self.pushButton_reset_counter.clicked.connect(self.on_reset_counter_clicked)
        self.pushButton_reboot.clicked.connect(self.on_reboot_button_clicked)
        self.pushButton_poweroff.clicked.connect(self.on_poweroff_button_clicked)

        self.pushButton_object_track.clicked.connect(self.on_track_cots_clicked)
        self.pushButton_show_anno.clicked.connect(self.on_show_anno_clicked)
        
    def on_show_anno_clicked(self):
        self.fpe.annotate = not self.fpe.annotate
        if self.fpe.annotate:
            self.pushButton_show_anno.setText("Showing Annotation")
        else:
            self.pushButton_show_anno.setText("Show Annotation")
        self.pushButton_show_anno.setChecked(self.fpe.annotate)    
    
    def on_reboot_button_clicked(self):
        self.exit_code = 888;
        self.MainWindow.close()

    def on_poweroff_button_clicked(self):
        self.exit_code = 999;
        self.MainWindow.close()
    
    def on_reset_counter_clicked(self):
        self.inference_backend.reset_object_count()
        self.track_id_patch_dict = {}
        self.label_track_cots.clear()

    def on_track_cots_clicked(self):
        self.inference_backend.set_enable_tracker(not self.inference_backend.get_enable_tracker())
        if self.inference_backend.get_enable_tracker():
            self.pushButton_object_track.setText("Tracking COTS")
        else:
            self.pushButton_object_track.setText("Track COTS")
        self.pushButton_object_track.setChecked(self.inference_backend.get_enable_tracker())

    def on_capture_clicked(self):
        self.pushButton_capture.setText("Capturing")
        self.pushButton_capture.setEnabled(False)
        self.capture_a_frame = True

    def on_start_clicked(self):
        self.log_started = not self.log_started
        if self.log_started:
            self.start_trip_time = datetime.now().strftime("%Y%m%d%H%M%S")
            self.trip_root_dir = 'trips'
            self.trip_name = 'trip'
            self.trip_dir = "%s/%s_%s" % (self.trip_root_dir, self.trip_name, self.start_trip_time)
            create_dir_if_not_exists(self.trip_dir)
            self.on_reset_counter_clicked()
        else:
            self.save_metadata()
        
        self.update_start_button()
        self.pushButton_new_trip.setEnabled(not self.log_started)
        self.pushButton_upload.setEnabled(not self.log_started)
        self.pushButton_start.setEnabled(self.log_started)
        self.pushButton_capture.setEnabled(self.log_started)

    def update_start_button(self):
        if self.log_started:
            self.pushButton_start.setText("Stop")
        else:
            self.pushButton_start.setText("Start")

    def on_new_trip_clicked(self):
        self.newTripDialog = NewTripDialog(None, self.sensor_manager)
        result = self.newTripDialog.exec()
        if result == QDialog.Accepted:
            self.metadata = {}
            self.metadata['latitude'] = self.newTripDialog.ui.lineEdit_latitude.text()
            self.metadata['longitude'] = self.newTripDialog.ui.lineEdit_longitude.text()
            self.metadata['cots_count'] = 0

            self.pushButton_start.setEnabled(True)
            self.pushButton_capture.setEnabled(True)

    def on_upload_clicked(self):
        self.uploadTripDialog = UploadTripDialog()
        result = self.uploadTripDialog.exec()
        if result == QDialog.Accepted:
            pass

    def on_sensitivity_change(self):
        conf_val = (100 - self.horizontalScrollBar_sensitivity.value()) / 100
        self.inference_backend.set_confidence_thresh(conf_val)
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
            if not self.log_started and len(self.metadata) > 0:
                json_filename = "meta_%s_%s_%s_%s_%s.json" % (
                    self.trip_name, self.start_trip_time, self.metadata['latitude'], self.metadata['longitude'], self.metadata['cots_count'])
                with open("%s/%s" % (self.trip_dir, json_filename), "w") as outfile:
                    json.dump(self.metadata, outfile)
                self.metadata = {}
                self.label_camview.clear()
                self.statusbar.showMessage('')
                self.label_camview.setText('Camera View')
        except Exception as e:
            Log.error(f"Saving metadata error: {e}")

    def update_status_bar(self, results):
        # Example: show info on status bar.
        pad_size = 35
        msg_str = f"  FPS: {results['fps']} ".ljust(pad_size)
        msg_str += f"Inference Time: {round(results['inference_time'] * 1000, 2)}ms ".ljust(pad_size)
        msg_str += f"Num COTS current frame: {round(results['n_objects'])} ".ljust(pad_size)
        msg_str += f"End-to-end time: {round(results['total_time'] * 1000, 2)}ms".ljust(pad_size)

        if self.pushButton_object_track.isChecked():
            msg_str += f"COTS count: {results['cots_cnt']}".ljust(pad_size) 
        self.statusbar.showMessage(msg_str)
        
    def save_results(self, results):
        # ---------- Handle image saving -----------
        # save processed frame
        currentTime = str(round(time.time()))
        file_prefix = f"{self.trip_name}_{self.start_trip_time}_{currentTime}"
        saveSensorData = False
        if self.log_started and results['n_objects'] > 0:
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

        if self.log_started and self.capture_a_frame:
            saveSensorData = True
            cv.imwrite(
                f"{self.trip_dir}/{file_prefix}_captured.jpg",
                results['raw_frame']
            )
            self.capture_a_frame = False
            self.pushButton_capture.setEnabled(True)
            self.pushButton_capture.setText("Capture")

        # Save sensor data into metadata
        if saveSensorData:
            self.metadata[currentTime] = {}
            self.metadata[currentTime]['temperature'] = self.sensor_manager.get_sensor_reading('temperature')

        
    def show_objects_current_frame(self, results):
        # ---------- Displaying COTS -----------
        cots_patch = np.zeros((160, 1280, 3), dtype=np.uint8)
        boxes = sorted(results['boxes'][:8], key=lambda b: b[1], reverse=True)
        boxes = sorted(boxes, key=lambda b: b[0])
        p_size = 160
        for idx, box in enumerate(boxes):
            kp = [int(x) for x in box]
            rec_range = max(kp[2] - kp[0], kp[3] - kp[1])
            patch = results['raw_frame'][kp[1]:kp[1] + rec_range, kp[0]:kp[0] + rec_range]
            try:
                patch = cv.resize(patch, (p_size, p_size))
            except Exception:
                pass
            x_pos = idx * p_size
            y_pox = 0
            cots_patch[y_pox:y_pox+p_size, x_pos:x_pos+p_size] = patch[:, :]

        patch_qt = QPixmap.fromImage(cvt_cv_to_qt(cots_patch, 1260, 160))
        self.label_cots.setPixmap(patch_qt)
        
    def show_tracked_objects(self, results):
        """
        Total drawable space is (660, 550)
        each patch is of size (110, 110) pixels (h, w)
        6x5 = 30 most recent detections will be shown in the UI
        """
        # ---------- Tracking COTS -------------
        if not self.pushButton_object_track.isChecked():
            return
        raw = results['raw_frame']
        for k, v in results['track_dict'].items():
            if k not in self.track_id_patch_dict:
                self.track_id_patch_dict[k] = np.zeros((110, 110, 3), dtype=np.uint8)
            try:
                rec_range = max(v[2] - v[0], v[3] - v[1])
                self.track_id_patch_dict[k] = cv.resize(raw[v[1]:v[1]+rec_range, v[0]:v[0]+rec_range], (110, 110))
            except Exception:
                pass
        
        cots_patch = np.zeros((660, 550, 3), dtype=np.uint8)
        self.track_id_patch_dict = dict(sorted(self.track_id_patch_dict.items(), reverse=True)[:30])
        for idx, (id, patch) in enumerate(self.track_id_patch_dict.items()):
            row = (idx // 5) * 110
            col = (idx % 5) * 110
            cots_patch[row:row+110, col:col+110] = patch
            bcolor = COLOR_PALETTE[id % len(COLOR_PALETTE)]
            cv.rectangle(cots_patch, (col+2, row+2), (col+108, row+108), bcolor, 4)
            cv.rectangle(cots_patch, (col+2, row+2), (col+35, row+20), bcolor, -1)
            cv.putText(cots_patch, str(id), (col+2, row+14), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [255, 255, 255], 1)
        
        patch_qt = QPixmap.fromImage(cvt_cv_to_qt(cots_patch, 550, 660))
        self.label_track_cots.setPixmap(patch_qt)
        
    def update_results_metadata(self, results):
        if self.log_started:
            self.metadata['cots_count'] = results['cots_cnt']

    def process_results(self):
        """
        Further result processing procedure goes here.
        """
        ret, results = self.fpe.get()
        if not ret:
            return
        
        self.update_status_bar(results)
        self.show_objects_current_frame(results)
        self.save_results(results)
        self.show_tracked_objects(results)
        self.update_results_metadata(results)

        self.put(results)

    def ask_stop_app(self, event):
        msg = QMessageBox()
        msg.setWindowTitle("Exit?")
        msg.setText("Confirm exit this application?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setIcon(QMessageBox.Warning)
        font = msg.font()
        font.setBold(True)
        font.setPointSize(50)
        msg.setFont(font)
        ret = msg.exec_()
        if ret == QMessageBox.Ok:
            Log.info("Program exit.")
            self.qt_app.closeAllWindows()
            event.accept()
        else:
            self.exit_code = 0
            event.ignore()

    def exit_procedure(self):
        Log.info(f"Exiting procedure in prrogress...")
        self.inference_backend.release_resrouce()
        if self.fpe:
            self.save_metadata()
            self.fpe.thread_run = False
            self.fpe.exit(0)
        if self.sensor_manager:
            self.sensor_manager.thread_stop()
        time.sleep(3)
        Log.info(f"Exiting procedure done.")

    def launch(self):
        self.MainWindow.show()
        Log.info("Launching the application...")
        if self.fpe:
            self.fpe.start()
        _exit_code = self.qt_app.exec_()
        self.exit_procedure()
        if self.exit_code == 999:  # poweroff
            os.system('poweroff')
        elif self.exit_code == 888:  # reboot
            os.system('reboot')
        return _exit_code


class FrameProcessingEngine(QThread, BufferPackedResult):
    sig_source = pyqtSignal(QImage)

    def __init__(self, inference_backend: InferenceBackend, sensor_manager: SensorManager, vid_file: None):
        QThread.__init__(self)
        BufferPackedResult.__init__(self)
        self.thread_run = True
        self.vid_mode = False
        self.vid_file = vid_file
        self.sensor_manager = sensor_manager
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
        self.annotate = True


    def run(self):  # Implement QThread function
        while self.thread_run:
            timer = time.time()
            ret, frame = self.cap.read()
            if self.vid_mode:
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
            results = self.inf_bkend.inference(frame)
            # copy an instance for display
            out_frame = results['out_frame'].copy()
            results['raw_frame'] = raw_frame
            results['total_time'] = time.time() - timer
            results['fps'] = round(1 / results['inference_time'])
            self.put(results)
            

            if self.annotate:
                temperature = self.sensor_manager.get_sensor_reading('temperature')
                # ; separated text, ; is line separator.
                frame_text = f"COTS: {results['n_objects']}; FPS: {results['fps']};Temperature: {temperature}"

                if self.inf_bkend.get_enable_tracker():
                    frame_text += f";COTS Count: {results['cots_cnt']}"
                out_frame = add_text_to_frame(out_frame, frame_text)
            self.sig_source.emit(cvt_cv_to_qt(out_frame))

        self.cap.release()


if __name__ == '__main__':
    video_file = sys.argv[1] if len(sys.argv) > 1 else None
    app = DetectorApp(video_file)
    exit_code = app.launch()
    Log.info(f"Exit code: {exit_code}")
    sys.exit(exit_code)
