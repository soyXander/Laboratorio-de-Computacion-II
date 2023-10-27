from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnCambiar.clicked.connect(self.on_cambiar_saludo)
    
    def on_cambiar_saludo(self):
        self.mensaje.setText("Chau Mundo!")

app = QApplication([])
windows = MiVentana()
windows.show()

app.exec()