from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnMostrar.clicked.connect(self.on_mostrar)
    
    def on_mostrar(self):
        nomCompleto = f"Nombre completo: {self.fldApellido.text()}, {self.fldNombre.text()}"
        self.nombreCompleto.setText(nomCompleto)

app = QApplication([])
window = MiVentana()

window.show()
app.exec()