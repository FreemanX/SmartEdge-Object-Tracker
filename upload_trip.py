from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QHeaderView, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QDateTime, Qt, pyqtSignal
from PyQt5 import QtCore, QtWidgets
from upload_trip_dialog_ui import Ui_NewTripDialog

from cloud.upload import *
from libs.utils import *
import threading
import time
from subprocess import call


class UploadTripDialog(QDialog):
    updateProgress = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewTripDialog()
        self.ui.setupUi(self)

        # setup UI default display
        self.setupDefaultUi()

        # setup signal 
        self.connectSignalSlots()
    
    def setupDefaultUi(self):
        self.setWindowTitle("Upload Trip")
        self.ui.tableWidget.sortItems(0, Qt.AscendingOrder)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Upload")
        self.ui.label_upload.setText("")
        self.setupTableWidget();

    def setupTableWidget(self):
        folderList, dateList = self.obtainTripsDetail()
        for i in range(len(dateList)):
            qDateTime = QDateTime.fromString(dateList[i], "yyyyMMddHHmmss")
            dtString = qDateTime.toString()
            if dtString == "":
                continue
            rowCount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowCount)
            rowItem = QTableWidgetItem(dtString)
            rowItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            rowItem.setCheckState(Qt.Unchecked)
            rowItem.setData(Qt.UserRole, folderList[i])
            self.ui.tableWidget.setItem(rowCount, 0, rowItem)
                
    def obtainTripsDetail(self):
        tripList = get_all_subdir("./trips")
        tripDateList = []
        for trip in tripList:
            tripDateRaw = trip.split("_")[1]
            tripDateList.append(tripDateRaw)
        return tripList, tripDateList

    def connectSignalSlots(self):
        self.updateProgress.connect(self.ui.label_upload.setText)
        self.ui.tableWidget.itemClicked.connect(self.onTableClicked)
        pass
            
    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)    
    def onTableClicked(self, it):
        state = not it.data(Qt.UserRole)
        checked = it.checkState() == Qt.Checked        
        it.setCheckState(Qt.Checked if not checked else Qt.Unchecked)

    def accept(self):
        thread = threading.Thread(target=self.uploadTrips)
        thread.start()
        thread.join()
        QDialog.accept(self)
    
    def uploadTrips(self):
        rowCount = self.ui.tableWidget.rowCount()
        uploadTrips = []
        for i in range(rowCount):
            rowItem = self.ui.tableWidget.item(i, 0)
            cs = rowItem.checkState()
            if cs == Qt.Checked:
                uploadTrips.append(rowItem.data(Qt.UserRole))
        
        count = 1
        for trip in uploadTrips:
            self.updateProgress.emit(f"({count}/{len(uploadTrips)}) Uploading Trip...")
            count += 1
            zipFile = "./trips/" + trip + ".tar"
            call(['tar', '-czf', zipFile, f"--directory=./trips/{trip}", "./"])
            #upload_binary(file, zipFile)

    def buttonClicked(self):
        pass
    
        
