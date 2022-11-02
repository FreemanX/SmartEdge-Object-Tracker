# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_trip_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTripDialog(object):
    def setupUi(self, NewTripDialog):
        NewTripDialog.setObjectName("NewTripDialog")
        NewTripDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        NewTripDialog.resize(1079, 421)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        NewTripDialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(NewTripDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_latitude = QtWidgets.QLabel(NewTripDialog)
        self.label_latitude.setObjectName("label_latitude")
        self.gridLayout.addWidget(self.label_latitude, 1, 0, 1, 1)
        self.lineEdit_longitude = QtWidgets.QLineEdit(NewTripDialog)
        self.lineEdit_longitude.setObjectName("lineEdit_longitude")
        self.gridLayout.addWidget(self.lineEdit_longitude, 2, 1, 1, 1)
        self.lineEdit_latitude = QtWidgets.QLineEdit(NewTripDialog)
        self.lineEdit_latitude.setObjectName("lineEdit_latitude")
        self.gridLayout.addWidget(self.lineEdit_latitude, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewTripDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 4)
        self.pushButton_getGPS = QtWidgets.QPushButton(NewTripDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_getGPS.sizePolicy().hasHeightForWidth())
        self.pushButton_getGPS.setSizePolicy(sizePolicy)
        self.pushButton_getGPS.setObjectName("pushButton_getGPS")
        self.gridLayout.addWidget(self.pushButton_getGPS, 1, 2, 2, 1)
        self.label_longitude = QtWidgets.QLabel(NewTripDialog)
        self.label_longitude.setObjectName("label_longitude")
        self.gridLayout.addWidget(self.label_longitude, 2, 0, 1, 1)
        self.label_header = QtWidgets.QLabel(NewTripDialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.gridLayout.addWidget(self.label_header, 0, 0, 1, 2)
        self.label_researcher = QtWidgets.QLabel(NewTripDialog)
        self.label_researcher.setObjectName("label_researcher")
        self.gridLayout.addWidget(self.label_researcher, 3, 0, 1, 1)
        self.comboBox_researcher = QtWidgets.QComboBox(NewTripDialog)
        self.comboBox_researcher.setObjectName("comboBox_researcher")
        self.gridLayout.addWidget(self.comboBox_researcher, 3, 1, 1, 2)

        self.retranslateUi(NewTripDialog)
        self.buttonBox.accepted.connect(NewTripDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(NewTripDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewTripDialog)

    def retranslateUi(self, NewTripDialog):
        _translate = QtCore.QCoreApplication.translate
        NewTripDialog.setWindowTitle(_translate("NewTripDialog", "Dialog"))
        self.label_latitude.setText(_translate("NewTripDialog", "Latitude"))
        self.pushButton_getGPS.setText(_translate("NewTripDialog", "Get GPS"))
        self.label_longitude.setText(_translate("NewTripDialog", "Longitude"))
        self.label_header.setText(_translate("NewTripDialog", "New Trip"))
        self.label_researcher.setText(_translate("NewTripDialog", "Researcher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTripDialog = QtWidgets.QDialog()
    ui = Ui_NewTripDialog()
    ui.setupUi(NewTripDialog)
    NewTripDialog.show()
    sys.exit(app.exec_())