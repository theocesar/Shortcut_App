from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget
import db_connect


class UpdtWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update shortcut")

        uic.loadUi('Ui/updt_short.ui', self)

        self.addB.clicked.connect(self.update_shortcut)

    def update_shortcut(self):
        name = self.name.text()
        path = self.path.text()

        db_connect.insert(name, path)

        return self.CloseWindow()
    
    def CloseWindow(self):
        return self.close()

    # Método fechar a window
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Escape:
            self.close()