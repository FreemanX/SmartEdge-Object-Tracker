from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtCore import QDateTime
from ui.new_trip_dialog_ui import Ui_NewTripDialog
from random import uniform

class NewTripDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewTripDialog()
        self.ui.setupUi(self)

        # setup UI default display
        self.setupDefaultUi()

        # setup signal 
        self.connectSignalSlots()
    
    def setupDefaultUi(self):
        self.setWindowTitle("New Log")

    def connectSignalSlots(self):
        self.ui.pushButton_getGPS.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        self.ui.lineEdit_latitude.setText(str(round(uniform(-18.456, -14.750), 6)))
        self.ui.lineEdit_longitude.setText(str(round(uniform(146.629, 151.033), 6)))

