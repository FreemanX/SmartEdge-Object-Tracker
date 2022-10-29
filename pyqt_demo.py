import sys

import numpy as np
import queue
import typing
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox

import pyqt_demo_ui as UI
from inference_backend import *
from libs.utils import *
from libs.Log import Log


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


class FrameProcessingEngine(QThread, BufferPackedResult):
    sig_source = pyqtSignal(QImage)

    def __init__(self, inference_backend: InferenceBackend, vid_file: None):
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

    def run(self):  # Implement QThread function
        while self.thread_run:
            timer = time.time()
            ret, frame = self.cap.read()
            if not ret and self.vid_mode:
                Log.info(f"End of video reached, reset to the first frame.")
                self.cap.release()
                self.cap = cv.VideoCapture(self.vid_file)
            elif not ret:
                Log.warning("Failed to get video frame from camera. Retrying...")
                continue
            if frame is None:
                continue

            results = self.inf_bkend.inference(frame)
            # copy an instance for display
            out_frame = results['out_frame'].copy()
            results['raw_frame'] = frame.copy()
            results['total_time'] = time.time() - timer
            self.put(results)
            # ; separated text, ; is line separator.
            frame_text = f"COTS: {results['n_objects']}; FPS: {round(1/results['inference_time'])};"
            out_frame = add_text_to_frame(out_frame, frame_text)
            self.sig_source.emit(cvt_cv_to_qt(out_frame))
        self.cap.release()


class DetectorApp(UI.Ui_MainWindow):
    def __init__(self, video_file: None):
        self.qt_app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        # fix the GUI window
        self.MainWindow.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.MainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.MainWindow.setWindowFlag(Qt.WindowMinimizeButtonHint, False)

        self.inference_backend = InferenceBackend()
        self.fpe = FrameProcessingEngine(self.inference_backend, video_file)

        self.set_ui_actions()

    def set_ui_actions(self):
        # ---------  Sample Action
        self.MainWindow.closeEvent = self.ask_stop_app
        self.pushButton_exit.clicked.connect(lambda: self.MainWindow.close())
        # ---------  Sample Action end

        self.fpe.sig_source.connect(self.update_pp_to_ui)

    def update_pp_to_ui(self, img):  # update processed frame to ui
        self.label_camview.setPixmap(QPixmap.fromImage(img))
        self.process_results()

    def process_results(self):
        """
        Further result processing procedure goes here.
        """
        ret, results = self.fpe.get()
        if not ret:
            return
        # Example: show info on status bar.
        pad_size = 35
        msg_str = f"FPS: {round(1 / results['inference_time'])}, ".ljust(pad_size)
        msg_str += f"Inference Time: {round(results['inference_time'] * 1000, 2)}ms, ".ljust(pad_size)
        msg_str += f"Num COTS: {round(results['n_objects'])}, ".ljust(pad_size)
        msg_str += f"End-to-end time: {round(results['total_time'] * 1000, 2)}ms".ljust(pad_size)
        self.statusbar.showMessage(msg_str)

    def ask_stop_app(self, event):
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

if __name__ == '__main__':
    video_file = sys.argv[1] if len(sys.argv) > 1 else None
    app = DetectorApp(video_file)
    exit_code = app.launch()
    Log.info(f"Exit code: {exit_code}")
    sys.exit(exit_code)