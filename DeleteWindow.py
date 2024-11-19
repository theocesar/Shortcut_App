from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget
import db_connect

class DeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete shortcut")

        uic.loadUi('Ui/del_short.ui', self)

        self.delB.clicked.connect(self.delete_shortcut)

    def delete_shortcut(self):
        name = self.name.text()

        db_connect.delete(name)

        return self.CloseWindow()
    
    def CloseWindow(self):
        return self.close()

    # Método fechar a window
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Escape:
            self.close()