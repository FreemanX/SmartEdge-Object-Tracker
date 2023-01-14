# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_ui.ui'
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
        self.label_camview.setGeometry(QtCore.QRect(20, 10, 1280, 720))
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
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_camview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camview.setObjectName("label_camview")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1729, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1350, 175, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.pushButton_capture.setGeometry(QtCore.QRect(1640, 175, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
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
        self.pushButton_new_trip.setGeometry(QtCore.QRect(1350, 115, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_new_trip.setFont(font)
        self.pushButton_new_trip.setStyleSheet("")
        self.pushButton_new_trip.setObjectName("pushButton_new_trip")
        self.horizontalScrollBar_sensitivity = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_sensitivity.setGeometry(QtCore.QRect(780, 760, 481, 61))
        self.horizontalScrollBar_sensitivity.setStyleSheet("QScrollBar:horizontal {\n"
"  border-radius:6px;\n"
"  border-color: none;\n"
"  border-width: 1px;\n"
"  border-style: solid;\n"
"  background-color: rgba(255, 255, 255,240);\n"
"  width: 1px;\n"
"  margin: 0px 10px 0 10px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    border-radius:14px;\n"
"    background-color: rgb(114, 159, 207);\n"
"    min-height: 30px;\n"
"    min-width: 45px;\n"
" }\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 0px;\n"
"    border-radius:5px;\n"
"    \n"
"    background-color: rgb(114, 159, 207);\n"
"    \n"
"    \n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  border: 0px;\n"
"    border-radius:5px;\n"
"    \n"
"    background-color: rgb(114, 159, 207);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;  \n"
" }")
        self.horizontalScrollBar_sensitivity.setMinimum(1)
        self.horizontalScrollBar_sensitivity.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_sensitivity.setInvertedAppearance(False)
        self.horizontalScrollBar_sensitivity.setObjectName("horizontalScrollBar_sensitivity")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 765, 321, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_sensitivity = QtWidgets.QLabel(self.centralwidget)
        self.label_sensitivity.setGeometry(QtCore.QRect(740, 765, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_sensitivity.setFont(font)
        self.label_sensitivity.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_sensitivity.setObjectName("label_sensitivity")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(1640, 115, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setStyleSheet("")
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.bg_color = QtWidgets.QLabel(self.centralwidget)
        self.bg_color.setGeometry(QtCore.QRect(1335, 250, 581, 751))
        self.bg_color.setAutoFillBackground(False)
        self.bg_color.setStyleSheet("background-color: rgb(211, 215, 207);\n"
"border-radius: 10px;")
        self.bg_color.setText("")
        self.bg_color.setObjectName("bg_color")
        self.header_bg_color = QtWidgets.QLabel(self.centralwidget)
        self.header_bg_color.setGeometry(QtCore.QRect(0, 20, 611, 101))
        palette = QtGui.QPalette()
        self.header_bg_color.setPalette(palette)
        self.header_bg_color.setStyleSheet("")
        self.header_bg_color.setText("")
        self.header_bg_color.setObjectName("header_bg_color")
        self.pushButton_reboot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reboot.setGeometry(QtCore.QRect(1530, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_reboot.setFont(font)
        self.pushButton_reboot.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_reboot.setObjectName("pushButton_reboot")
        self.pushButton_poweroff = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_poweroff.setGeometry(QtCore.QRect(1330, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_poweroff.setFont(font)
        self.pushButton_poweroff.setStyleSheet("background-color: rgb(206, 92, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_poweroff.setObjectName("pushButton_poweroff")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1340, 65, 321, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.bg_color_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_color_2.setGeometry(QtCore.QRect(1335, 70, 581, 170))
        self.bg_color_2.setAutoFillBackground(False)
        self.bg_color_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(238, 238, 236);")
        self.bg_color_2.setText("")
        self.bg_color_2.setObjectName("bg_color_2")
        self.label_cots = QtWidgets.QLabel(self.centralwidget)
        self.label_cots.setGeometry(QtCore.QRect(20, 840, 1280, 160))
        self.label_cots.setStyleSheet("")
        self.label_cots.setText("")
        self.label_cots.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cots.setObjectName("label_cots")
        self.label_track_cots = QtWidgets.QLabel(self.centralwidget)
        self.label_track_cots.setGeometry(QtCore.QRect(1350, 329, 550, 660))
        self.label_track_cots.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_track_cots.setText("")
        self.label_track_cots.setObjectName("label_track_cots")
        self.widget_error_screen = QtWidgets.QWidget(self.centralwidget)
        self.widget_error_screen.setEnabled(True)
        self.widget_error_screen.setGeometry(QtCore.QRect(20, 10, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(25)
        self.widget_error_screen.setFont(font)
        self.widget_error_screen.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(9, 26, 138);")
        self.widget_error_screen.setObjectName("widget_error_screen")
        self.label_4 = QtWidgets.QLabel(self.widget_error_screen)
        self.label_4.setGeometry(QtCore.QRect(540, 159, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(9, 26, 138);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_error_screen)
        self.label_5.setGeometry(QtCore.QRect(210, 230, 871, 251))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_error_screen)
        self.label_6.setGeometry(QtCore.QRect(270, 500, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_reset_counter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset_counter.setGeometry(QtCore.QRect(1710, 265, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
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
"*/")
        self.pushButton_reset_counter.setObjectName("pushButton_reset_counter")
        self.pushButton_show_anno = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_anno.setGeometry(QtCore.QRect(70, 755, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_show_anno.setFont(font)
        self.pushButton_show_anno.setStyleSheet("QPushButton:checked{\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 253, 114, 255), stop:1 rgba(76, 255, 114, 150));\n"
"     border-radius: 20px;\n"
"}\n"
"QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(184, 184, 184);\n"
"     border-radius: 20px;\n"
"}QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_show_anno.setCheckable(True)
        self.pushButton_show_anno.setChecked(False)
        self.pushButton_show_anno.setObjectName("pushButton_show_anno")
        self.pushButton_object_track = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_object_track.setGeometry(QtCore.QRect(1355, 265, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_object_track.setFont(font)
        self.pushButton_object_track.setStyleSheet("QPushButton:checked{\n"
"     background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(0, 253, 114, 255), stop:1 rgba(76, 255, 114, 150));\n"
"     border-radius: 20px;\n"
"}\n"
"QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(184, 184, 184);\n"
"     border-radius: 20px;\n"
"}QPushButton:pressed { \n"
"background-color: qlineargradient(spread:pad, x1:0.483727, y1:1, x2:0.495, y2:0, stop:0 rgba(76, 178, 158, 255), stop:1 rgba(76, 255, 0, 0));\n"
"    color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"}")
        self.pushButton_object_track.setCheckable(True)
        self.pushButton_object_track.setChecked(False)
        self.pushButton_object_track.setObjectName("pushButton_object_track")
        self.label_detect_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_detect_bg.setGeometry(QtCore.QRect(0, 0, 1320, 1010))
        self.label_detect_bg.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.label_detect_bg.setText("")
        self.label_detect_bg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_detect_bg.setObjectName("label_detect_bg")
        self.label_detect_bg.raise_()
        self.bg_color_2.raise_()
        self.header_bg_color.raise_()
        self.bg_color.raise_()
        self.label_camview.raise_()
        self.pushButton_exit.raise_()
        self.pushButton_start.raise_()
        self.pushButton_capture.raise_()
        self.pushButton_new_trip.raise_()
        self.pushButton_upload.raise_()
        self.pushButton_reboot.raise_()
        self.pushButton_poweroff.raise_()
        self.label_2.raise_()
        self.label_cots.raise_()
        self.label_track_cots.raise_()
        self.widget_error_screen.raise_()
        self.pushButton_reset_counter.raise_()
        self.label.raise_()
        self.horizontalScrollBar_sensitivity.raise_()
        self.label_sensitivity.raise_()
        self.pushButton_show_anno.raise_()
        self.pushButton_object_track.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
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
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_capture.setText(_translate("MainWindow", "Capture"))
        self.pushButton_new_trip.setText(_translate("MainWindow", "New Log"))
        self.label.setText(_translate("MainWindow", "Detection Sensitivity:"))
        self.label_sensitivity.setText(_translate("MainWindow", "0"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.pushButton_reboot.setText(_translate("MainWindow", "Reboot"))
        self.pushButton_poweroff.setText(_translate("MainWindow", "Power off"))
        self.label_2.setText(_translate("MainWindow", "Detection Logging"))
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
        self.pushButton_show_anno.setText(_translate("MainWindow", "Show Annotation"))
        self.pushButton_object_track.setText(_translate("MainWindow", "Track COTS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

