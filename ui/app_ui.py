# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_demo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1030)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1030))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1030))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/unsw_logo_sqr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Australia))
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label_camview = QtWidgets.QLabel(self.centralwidget)
        self.label_camview.setGeometry(QtCore.QRect(20, 140, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camview.sizePolicy().hasHeightForWidth())
        self.label_camview.setSizePolicy(sizePolicy)
        self.label_camview.setMinimumSize(QtCore.QSize(1280, 720))
        self.label_camview.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setPointSize(120)
        font.setBold(True)
        font.setWeight(75)
        self.label_camview.setFont(font)
        self.label_camview.setAutoFillBackground(False)
        self.label_camview.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.label_camview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camview.setObjectName("label_camview")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1719, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(20, 30, 191, 81))
        self.label_logo.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("res/unsw_logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_app = QtWidgets.QLabel(self.centralwidget)
        self.label_app.setGeometry(QtCore.QRect(230, 40, 1100, 51))
        font = QtGui.QFont()
        font.setPointSize(75)
        font.setBold(True)
        font.setWeight(75)
        self.label_app.setFont(font)
        self.label_app.setObjectName("label_app")
        self.label_team = QtWidgets.QLabel(self.centralwidget)
        self.label_team.setGeometry(QtCore.QRect(1040, 100, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setItalic(True)
        self.label_team.setFont(font)
        self.label_team.setObjectName("label_team")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1340, 185, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("/*\n"
"QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(201, 201, 201, 255));\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(225, 225, 225, 255));\n"
"     border-radius: 12px;\n"
"}\n"
"*/\n"
"")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_capture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_capture.setGeometry(QtCore.QRect(1630, 185, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_capture.setFont(font)
        self.pushButton_capture.setStyleSheet("/*\n"
"QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(201, 201, 201, 255));\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(225, 225, 225, 255));\n"
"     border-radius: 12px;\n"
"}\n"
"*/\n"
"")
        self.pushButton_capture.setObjectName("pushButton_capture")
        self.pushButton_new_trip = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_new_trip.setGeometry(QtCore.QRect(1340, 125, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_new_trip.setFont(font)
        self.pushButton_new_trip.setStyleSheet("")
        self.pushButton_new_trip.setObjectName("pushButton_new_trip")
        self.horizontalScrollBar_sensitivity = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_sensitivity.setGeometry(QtCore.QRect(1335, 355, 550, 61))
        self.horizontalScrollBar_sensitivity.setStyleSheet("QScrollBar:horizontal {\n"
"  border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,200);\n"
"  width: 1px;\n"
"  margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    /*  background-color: rgba(16, 104, 106,200); */\n"
"    \n"
"    background-color: rgb(52, 101, 164);\n"
"\n"
"    min-height: 30px;\n"
"    min-width: 45px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px;\n"
"    border-radius:5px;\n"
"    /* background-color: rgb(76, 178, 158); */\n"
"    \n"
"    background-color: rgb(32, 74, 135);\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 1px;\n"
"    border-radius:5px;\n"
"    /* background-color: rgb(76, 178, 158); */\n"
"    \n"
"    background-color: rgb(32, 74, 135);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_sensitivity.setMinimum(1)
        self.horizontalScrollBar_sensitivity.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_sensitivity.setObjectName("horizontalScrollBar_sensitivity")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1335, 305, 321, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_sensitivity = QtWidgets.QLabel(self.centralwidget)
        self.label_sensitivity.setGeometry(QtCore.QRect(1590, 305, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_sensitivity.setFont(font)
        self.label_sensitivity.setObjectName("label_sensitivity")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(1630, 125, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setStyleSheet("")
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.bg_color = QtWidgets.QLabel(self.centralwidget)
        self.bg_color.setGeometry(QtCore.QRect(1319, 260, 581, 741))
        self.bg_color.setAutoFillBackground(False)
        self.bg_color.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.bg_color.setText("")
        self.bg_color.setObjectName("bg_color")
        self.header_bg_color = QtWidgets.QLabel(self.centralwidget)
        self.header_bg_color.setGeometry(QtCore.QRect(0, 20, 1301, 101))
        palette = QtGui.QPalette()
        self.header_bg_color.setPalette(palette)
        self.header_bg_color.setStyleSheet("")
        self.header_bg_color.setText("")
        self.header_bg_color.setObjectName("header_bg_color")
        self.pushButton_reboot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reboot.setGeometry(QtCore.QRect(1520, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_reboot.setFont(font)
        self.pushButton_reboot.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_reboot.setObjectName("pushButton_reboot")
        self.pushButton_poweroff = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_poweroff.setGeometry(QtCore.QRect(1320, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_poweroff.setFont(font)
        self.pushButton_poweroff.setStyleSheet("background-color: rgb(206, 92, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_poweroff.setObjectName("pushButton_poweroff")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1330, 75, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.bg_color_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_color_2.setGeometry(QtCore.QRect(1320, 80, 580, 170))
        self.bg_color_2.setAutoFillBackground(False)
        self.bg_color_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.bg_color_2.setText("")
        self.bg_color_2.setObjectName("bg_color_2")
        self.label_cots = QtWidgets.QLabel(self.centralwidget)
        self.label_cots.setGeometry(QtCore.QRect(20, 862, 1280, 140))
        self.label_cots.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_cots.setText("")
        self.label_cots.setObjectName("label_cots")
        self.checkBox_obj_tracking = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_obj_tracking.setGeometry(QtCore.QRect(1340, 450, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_obj_tracking.setFont(font)
        self.checkBox_obj_tracking.setStyleSheet("QCheckBox::indicator { width: 30px; height: 30px;}")
        self.checkBox_obj_tracking.setObjectName("checkBox_obj_tracking")
        self.label_track_cots = QtWidgets.QLabel(self.centralwidget)
        self.label_track_cots.setGeometry(QtCore.QRect(1335, 495, 550, 500))
        self.label_track_cots.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_track_cots.setText("")
        self.label_track_cots.setObjectName("label_track_cots")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1330, 260, 381, 50))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.widget_error_screen = QtWidgets.QWidget(self.centralwidget)
        self.widget_error_screen.setEnabled(True)
        self.widget_error_screen.setGeometry(QtCore.QRect(20, 140, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(25)
        self.widget_error_screen.setFont(font)
        self.widget_error_screen.setStyleSheet("background-color: rgb(9, 26, 138);")
        self.widget_error_screen.setObjectName("widget_error_screen")
        self.label_4 = QtWidgets.QLabel(self.widget_error_screen)
        self.label_4.setGeometry(QtCore.QRect(540, 159, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(9, 26, 138);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_error_screen)
        self.label_5.setGeometry(QtCore.QRect(210, 230, 871, 251))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(40)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_error_screen)
        self.label_6.setGeometry(QtCore.QRect(270, 500, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(40)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_reset_counter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset_counter.setGeometry(QtCore.QRect(1695, 435, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_reset_counter.setFont(font)
        self.pushButton_reset_counter.setStyleSheet("/*\n"
"QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(201, 201, 201, 255));\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(225, 225, 225, 255));\n"
"     border-radius: 12px;\n"
"}\n"
"*/\n"
"")
        self.pushButton_reset_counter.setObjectName("pushButton_reset_counter")
        self.bg_color_2.raise_()
        self.header_bg_color.raise_()
        self.bg_color.raise_()
        self.label_camview.raise_()
        self.pushButton_exit.raise_()
        self.label_logo.raise_()
        self.label_app.raise_()
        self.label_team.raise_()
        self.pushButton_start.raise_()
        self.pushButton_capture.raise_()
        self.pushButton_new_trip.raise_()
        self.horizontalScrollBar_sensitivity.raise_()
        self.label.raise_()
        self.label_sensitivity.raise_()
        self.pushButton_upload.raise_()
        self.pushButton_reboot.raise_()
        self.pushButton_poweroff.raise_()
        self.label_2.raise_()
        self.label_cots.raise_()
        self.checkBox_obj_tracking.raise_()
        self.label_track_cots.raise_()
        self.label_3.raise_()
        self.widget_error_screen.raise_()
        self.pushButton_reset_counter.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(138, 226, 52);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crown-of-Thorns Starfish Realtime Detector"))
        self.label_camview.setText(_translate("MainWindow", "Camera View"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.label_app.setText(_translate("MainWindow", "Crown-of-Thorns Starfish Realtime Detector"))
        self.label_team.setText(_translate("MainWindow", "COMP6733 Team SmartEdge"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_capture.setText(_translate("MainWindow", "Capture"))
        self.pushButton_new_trip.setText(_translate("MainWindow", "New Log"))
        self.label.setText(_translate("MainWindow", "Detection Sensitivity:"))
        self.label_sensitivity.setText(_translate("MainWindow", "0"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.pushButton_reboot.setText(_translate("MainWindow", "Reboot"))
        self.pushButton_poweroff.setText(_translate("MainWindow", "Power off"))
        self.label_2.setText(_translate("MainWindow", "Detection Logging"))
        self.checkBox_obj_tracking.setText(_translate("MainWindow", " Track COTS"))
        self.label_3.setText(_translate("MainWindow", "Detection Control Panel"))
        self.label_4.setText(_translate("MainWindow", "Input Error"))
        self.label_5.setText(_translate("MainWindow", " A fatal exceptioin has occured when trying to connect to the camerea or load\n"
" the video file. Please do the following and try again. \n"
"\n"
"\n"
"       *    Check the connection to the camerea. \n"
"\n"
"       *    Make sure you have provided the correct video file."))
        self.label_6.setText(_translate("MainWindow", "Press Exit button to terminate this applicatioin _"))
        self.pushButton_reset_counter.setText(_translate("MainWindow", "Reset counter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
