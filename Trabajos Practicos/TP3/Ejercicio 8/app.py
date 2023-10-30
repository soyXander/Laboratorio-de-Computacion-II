from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnMoverDer.clicked.connect(self.on_mover_derecha)
        self.btnMoverIzq.clicked.connect(self.on_mover_izquierda)
        self.checkCount()
        
    def on_mover_derecha(self):
        row = self.listaIzquierda.currentRow()
        if row >= 0:
            item = self.listaIzquierda.takeItem(row)
            self.listaDerecha.addItem(item)
        self.checkCount()
            
    def on_mover_izquierda(self):
        row = self.listaDerecha.currentRow()
        if row >= 0:
            item = self.listaDerecha.takeItem(row)
            self.listaIzquierda.addItem(item)
        self.checkCount()

    def checkCount(self):
        if self.listaIzquierda.count() == 0:
            self.btnMoverDer.setEnabled(False)
        else:
            self.btnMoverDer.setEnabled(True)
            
        if self.listaDerecha.count() == 0:
            self.btnMoverIzq.setEnabled(False)
        else:
            self.btnMoverIzq.setEnabled(True)
        
app = QApplication([])
window = MiVentana()

window.show()
app.exec()