# Import modules
from PyQt5 import uic
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from sys import exit as sysExit
from EditWindow import EditWindow
import os
import db_connect



class ShortApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega o arquivo .ui
        uic.loadUi('Ui/main_window.ui', self)

        db_connect.create_table()

        # Conectar os botões e campos de texto a funções
        self.searchB.clicked.connect(self.findShortCut)  
        self.editB.clicked.connect(self.ShowEditWindow)  

        # Criar a janela de edição
        self.edit = EditWindow()

    def findShortCut(self):
        rows = db_connect.read_all()

        for row in rows:
            shortcut_name = row[0]  
            shortcut_path = row[1]  

            if os.path.exists(shortcut_path):
                for file in os.listdir(shortcut_path):
                    new_name = file.lower()

                    if new_name.startswith(shortcut_name.lower()):
                        filepath = os.path.join(shortcut_path, file)
                        return os.startfile(filepath)  
            else:
                print(f"O diretório {shortcut_path} não existe.")


    # Método para ativar a busca com "Enter"
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return or keyEvent.key() == Qt.Key_Enter:
            self.findShortCut()
        elif keyEvent.key() == Qt.Key_Escape:
            self.close()

    # Método para exibir a janela de edição
    def ShowEditWindow(self):
        self.edit.show()

if __name__ == "__main__":



    # Criar a aplicação
    app = QApplication([])
    main_window = ShortApp()

    # Exibir a janela principal
    main_window.show()
    sysExit(app.exec_())
