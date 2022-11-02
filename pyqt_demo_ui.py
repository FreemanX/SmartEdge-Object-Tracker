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
        self.label_camview.setGeometry(QtCore.QRect(20, 100, 1600, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camview.sizePolicy().hasHeightForWidth())
        self.label_camview.setSizePolicy(sizePolicy)
        self.label_camview.setMinimumSize(QtCore.QSize(1600, 900))
        self.label_camview.setMaximumSize(QtCore.QSize(1600, 900))
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
        self.pushButton_exit.setGeometry(QtCore.QRect(1640, 10, 260, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(20, 10, 191, 81))
        self.label_logo.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("res/unsw_logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_app = QtWidgets.QLabel(self.centralwidget)
        self.label_app.setGeometry(QtCore.QRect(240, 20, 1100, 51))
        font = QtGui.QFont()
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label_app.setFont(font)
        self.label_app.setObjectName("label_app")
        self.label_team = QtWidgets.QLabel(self.centralwidget)
        self.label_team.setGeometry(QtCore.QRect(1190, 65, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setItalic(True)
        self.label_team.setFont(font)
        self.label_team.setObjectName("label_team")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1640, 820, 260, 80))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_capture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_capture.setGeometry(QtCore.QRect(1640, 920, 260, 80))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_capture.setFont(font)
        self.pushButton_capture.setStyleSheet("")
        self.pushButton_capture.setObjectName("pushButton_capture")
        self.pushButton_new_trip = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_new_trip.setGeometry(QtCore.QRect(1640, 100, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_new_trip.setFont(font)
        self.pushButton_new_trip.setStyleSheet("")
        self.pushButton_new_trip.setObjectName("pushButton_new_trip")
        self.horizontalScrollBar_sensitivity = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_sensitivity.setGeometry(QtCore.QRect(1640, 720, 260, 80))
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
        self.label.setGeometry(QtCore.QRect(1640, 670, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_sensitivity = QtWidgets.QLabel(self.centralwidget)
        self.label_sensitivity.setGeometry(QtCore.QRect(1770, 670, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_sensitivity.setFont(font)
        self.label_sensitivity.setObjectName("label_sensitivity")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload.setGeometry(QtCore.QRect(1640, 160, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setStyleSheet("")
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.scrollArea_cots = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_cots.setGeometry(QtCore.QRect(1640, 230, 261, 441))
        self.scrollArea_cots.setWidgetResizable(True)
        self.scrollArea_cots.setObjectName("scrollArea_cots")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_cots.setWidget(self.scrollAreaWidgetContents)
        self.bg_color = QtWidgets.QLabel(self.centralwidget)
        self.bg_color.setGeometry(QtCore.QRect(1630, 220, 280, 790))
        self.bg_color.setAutoFillBackground(False)
        self.bg_color.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.bg_color.setText("")
        self.bg_color.setObjectName("bg_color")
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
        self.scrollArea_cots.raise_()
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
        self.pushButton_new_trip.setText(_translate("MainWindow", "New Trip"))
        self.label.setText(_translate("MainWindow", "Sensitivity:"))
        self.label_sensitivity.setText(_translate("MainWindow", "0"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

