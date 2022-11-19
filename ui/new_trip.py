from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtCore import QDateTime
from ui.new_trip_dialog_ui import Ui_NewTripDialog
from random import uniform
from sensor.SensorManager import SensorManager

class NewTripDialog(QDialog):
    def __init__(self, parent=None, sensor_manager: SensorManager = None):
        super().__init__(parent)
        self.ui = Ui_NewTripDialog()
        self.ui.setupUi(self)
        self.sensor_manager = sensor_manager

        # setup UI default display
        self.setupDefaultUi()

        # setup signal 
        self.connectSignalSlots()
    
    def setupDefaultUi(self):
        self.setWindowTitle("New Log")

    def connectSignalSlots(self):
        self.ui.pushButton_getGPS.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        self.ui.lineEdit_latitude.setText(self.sensor_manager.get_sensor_reading('latitude'))
        self.ui.lineEdit_longitude.setText(self.sensor_manager.get_sensor_reading('longitude'))

