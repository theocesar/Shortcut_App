# Import modules
from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
import db_connect
from AddWindow import AddWindow
from DeleteWindow import DeleteWindow
from UpdtWindow import UpdtWindow


class EditWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit shortcuts")

        uic.loadUi('Ui/edit.ui', self)

        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Path"])
        self.loadData()

        self.add_short = AddWindow()
        self.addB.clicked.connect(self.ShowAddWindow)

        self.delete_short = DeleteWindow()
        self.deleteB.clicked.connect(self.ShowDeleteWindow)

        self.updt_short = UpdtWindow()
        self.updateB.clicked.connect(self.ShowUpdateWindow)

        self.reloadB.clicked.connect(self.loadData)

    def loadData(self):
        rows = db_connect.read_all()
        
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(2)  

        for tablerow, row in enumerate(rows):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            

    def CloseWindow(self):
        return self.close()

    # Método fechar a window
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Escape:
            self.close()

    def ShowAddWindow(self):
        return self.add_short.show()

    def ShowDeleteWindow(self):
        return self.delete_short.show()
    
    def ShowUpdateWindow(self):
        return self.updt_short.show()