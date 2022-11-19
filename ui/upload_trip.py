from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QHeaderView, QTableWidget, QTableWidgetItem, QPushButton, QAbstractItemView, QMessageBox
from PyQt5.QtCore import QDateTime, Qt, pyqtSignal, QObject
from PyQt5 import QtCore, QtWidgets
from ui.upload_trip_dialog_ui import Ui_NewTripDialog

from cloud.upload import *
from libs.utils import *
import threading
import time
import shutil

class Helper(QObject):
    data_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

helper = Helper()

class UploadTripDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewTripDialog()
        self.ui.setupUi(self)
        
        # variable
        self.selected_item_count = 0
        self.can_checked = True

        # setup UI default display
        self.setupDefaultUi()

        # setup signal 
        self.connectSignalSlots()
    
    def setupDefaultUi(self):
        self.setWindowTitle("Upload Trip")
        self.ui.tableWidget.sortItems(0, Qt.AscendingOrder)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Upload")
        self.ui.label_upload.setText("No Selected")
        self.setupTableWidget()

    def setupTableWidget(self):
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.ui.tableWidget.setStyleSheet("QAbstractItemView::indicator { width: 20px;height:20px;} QTableWidget::item{width: 20px;height: 20px;} ")

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
        tripTrimmedList = []
        tripList.sort(reverse=True)
        for trip in tripList:
            tripnameList = trip.split("_")
            if len(tripnameList) == 1:
                continue
            tripTrimmedList.append(trip)
            tripDateRaw = trip.split("_")[1]
            tripDateList.append(tripDateRaw)
        return tripTrimmedList, tripDateList

    def connectSignalSlots(self):
        self.ui.tableWidget.itemClicked.connect(self.onTableClicked)
        self.ui.tableWidget.itemChanged.connect(self.onTableItemChanged)
            
    @QtCore.pyqtSlot(QtWidgets.QTableWidgetItem)
    def onTableClicked(self, it):
        if self.can_checked:
            state = not it.data(Qt.UserRole)
            checked = it.checkState() == Qt.Checked
            it.setCheckState(Qt.Checked if not checked else Qt.Unchecked)

    def onTableItemChanged(self, it):
        state = not it.data(Qt.UserRole)
        checked = it.checkState() == Qt.Checked        
        if not self.can_checked:
            self.ui.tableWidget.blockSignals(True)
            it.setCheckState(Qt.Checked if not checked else Qt.Unchecked)
            self.ui.tableWidget.blockSignals(False)
        else:
            self.selected_item_count += (1 if checked else -1)
            self.ui.label_upload.setText(f'{self.selected_item_count} Selected' if self.selected_item_count > 0 else 'No Selected')

    def onDataSignal(self, text):
        self.ui.label_upload.setText(text)
        print(text)

    def onErrorSignal(self, error):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error")
        msgBox.setText(str(error))
        msgBox.setStandardButtons(QMessageBox.Ok)
        font = msgBox.font()
        font.setBold(True)
        font.setPointSize(50)
        msgBox.setFont(font)
        msgBox.exec()

    def accept(self):
        thread = threading.Thread(target=self.uploadTrips)
        helper.data_signal.connect(self.onDataSignal)
        helper.error_signal.connect(self.onErrorSignal)
        thread.start()
    
    def uploadTrips(self):
        self.can_checked = False
        rowCount = self.ui.tableWidget.rowCount()
        uploadTripList = []
        for i in range(rowCount):
            rowItem = self.ui.tableWidget.item(i, 0)
            cs = rowItem.checkState()
            if cs == Qt.Checked:
                uploadTripList.append(rowItem.data(Qt.UserRole))
        
        count = 0
        for trip in uploadTripList:
            count += 1            
            helper.data_signal.emit(f"({count}/{len(uploadTripList)}) Zipping trip...")
            zipPath = f'./trips/export/zip_{trip}'            
            shutil.make_archive(zipPath, 'zip', f'./trips/{trip}')
            helper.data_signal.emit(f"({count}/{len(uploadTripList)}) Uploading trip...")
            try:
                upload_s3(f'{zipPath}.zip', f'zip_{trip}.zip')
            except Exception as err:
                helper.error_signal.emit(str(err))
                
        helper.data_signal.emit(f"({count}/{len(uploadTripList)}) Done")
        QDialog.accept(self)

    def buttonClicked(self):
        pass
    
        
