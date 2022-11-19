import os
import platform
import time
from datetime import datetime
from os import walk
from pathlib import Path

import cv2 as cv
import psutil
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage
import random 


# system related
def get_ram_size_gb():
    return psutil.virtual_memory().total / 2 ** 30


# file related
def rm_rf_dir(path_to_dir):
    os.system(f"rm -rf {path_to_dir}")


def get_creation_time(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def rm_empty_dirs(root):
    folders = list(os.walk(root))[1:]
    for folder in folders:
        if not folder[2]:
            os.rmdir(folder[0])


def path_exist(local_path: str):
    return Path(local_path).exists()


def create_dir_if_not_exists(dir_path: str) -> None:
    Path(dir_path).mkdir(parents=True, exist_ok=True)


def get_all_subdir(dir_path: str):
    if not path_exist(dir_path):
        return None
    dirs = list(next(walk(dir_path))[1])
    return dirs


def get_all_files(dir_path: str):
    if not path_exist(dir_path):
        return []
    files = list(next(walk(dir_path))[2])
    return files


# time related
_DATE_FORMAT = '%Y%m%d %H:%M:%S'
_FILE_DATE_FORMAT = '%Y%m%d%H%M%S'


def cvt_to_date_fmt(time_value):
    return str(datetime.fromtimestamp(time_value).strftime(_DATE_FORMAT))


def cvt_to_file_fmt(time_value):
    return str(datetime.fromtimestamp(time_value).strftime(_FILE_DATE_FORMAT))


def get_current_time():
    return cvt_to_date_fmt(time.time())


def get_current_time_filename():
    return cvt_to_file_fmt(time.time())


def get_date_today():
    return datetime.now().strftime('%Y-%m-%d')


# cv related
def gstreamer_pipeline(
        sensor_id=0,
        capture_width=1280,
        capture_height=720,
        display_width=1280,
        display_height=720,
        frame_rate=60,
        flip_method=2,
):
    """
    Used by Nvidia Jetson Nano
    """
    return (
            "nvarguscamerasrc sensor-id=%d ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                sensor_id,
                capture_width,
                capture_height,
                frame_rate,
                flip_method,
                display_width,
                display_height,
            )
    )


def cvt_cv_to_qt(cv_frame, scale_w=1280, scale_h=720) -> QImage:
    cv_frame_rgb = cv.cvtColor(cv_frame, cv.COLOR_BGR2RGB)
    h, w, ch = cv_frame_rgb.shape
    bytes_per_line = ch * w
    qt_frame = QImage(cv_frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
    qt_frame = qt_frame.copy()
    p = qt_frame.scaled(scale_w, scale_h, Qt.KeepAspectRatio)
    return p


def add_text_to_frame(frame, text: str):
    for idx, d_str in enumerate(text.split(';')):
        cv.putText(frame, d_str, (10, 50 + 30 * idx), cv.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 255), 2)
    return frame
