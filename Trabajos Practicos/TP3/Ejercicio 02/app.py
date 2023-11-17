from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnArriba.clicked.connect(self.on_arriba)
        self.btnDerecha.clicked.connect(self.on_derecha)
        self.btnAbajo.clicked.connect(self.on_abajo)
        self.btnIzquierda.clicked.connect(self.on_izquierda)
    
    def on_arriba(self):
        self.btnArriba.setEnabled(False)
        self.btnDerecha.setEnabled(True)

    def on_derecha(self):
        self.btnDerecha.setEnabled(False)
        self.btnAbajo.setEnabled(True)

    def on_abajo(self):
        self.btnAbajo.setEnabled(False)
        self.btnIzquierda.setEnabled(True)

    def on_izquierda(self):
        self.btnIzquierda.setEnabled(False)
        self.btnArriba.setEnabled(True)

app = QApplication([])
window = MiVentana()

window.show()
app.exec()