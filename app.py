# Import modules
from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
import db_connect
from sys import exit as sysExit
import os
import sys


def resource_path(relative_path):
    """Obtém o caminho absoluto do recurso, considerando o executável."""
    if hasattr(sys, '_MEIPASS'):  # Diretório temporário criado pelo PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class ShortApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega o arquivo .ui
        uic.loadUi(resource_path('main_window.ui'), self)

        db_connect.create_table()

        # Conectar os botões e campos de texto a funções
        self.searchB.clicked.connect(self.findShortCut)
        self.editB.clicked.connect(self.ShowEditWindow)

        # Criar a janela de edição
        self.edit = EditWindow()

    def findShortCut(self):
        name_input = self.file_name.text()  
        path_input = self.shortcut.text()  

        if not name_input or not path_input:
            print("Por favor, preencha os campos de nome e caminho.")
            return

        rows = db_connect.read_all()

        for row in rows:
            shortcut_name = row[0]
            shortcut_path = row[1]

            if path_input == shortcut_name:
                for file in os.listdir(shortcut_path):
                    new_name = file.lower()
                
                    if new_name.startswith(name_input.lower()):
                        filepath = os.path.join(shortcut_path, file)
                        return os.startfile(filepath)


    # Método para ativar a busca com "Enter"
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return or keyEvent.key() == Qt.Key_Enter:
            self.findShortCut()
        elif keyEvent.key() == Qt.Key_Escape:
            self.close()

    # Método para exibir a janela de edição
    def ShowEditWindow(self):
        self.edit.show()


class EditWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit shortcuts")

        uic.loadUi(resource_path('edit.ui'), self)

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


class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add shortcut")

        uic.loadUi(resource_path('add_short.ui'), self)

        self.addB.clicked.connect(self.add_shortcut)

    def add_shortcut(self):
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


class DeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete shortcut")

        uic.loadUi(resource_path('del_short.ui'), self)

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


class UpdtWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update shortcut")

        uic.loadUi(resource_path('updt_short.ui'), self)

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


if __name__ == "__main__":

    # Criar a aplicação
    app = QApplication([])
    main_window = ShortApp()

    # Exibir a janela principal
    main_window.show()
    sysExit(app.exec_())
