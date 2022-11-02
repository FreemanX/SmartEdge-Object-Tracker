from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtCore import QDateTime
from new_trip_dialog_ui import Ui_NewTripDialog
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
        self.setWindowTitle("New Trip")

    def connectSignalSlots(self):
        self.ui.pushButton_getGPS.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        self.ui.lineEdit_latitude.setText(str(uniform(-180, 180)))
        self.ui.lineEdit_longitude.setText(str(uniform(-90, 90)))
    
        
