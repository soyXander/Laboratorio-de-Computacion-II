from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnCalcular.clicked.connect(self.on_calcular)

    def on_calcular(self):
        if self.lomitoCarne.isChecked():
            total = 500
        elif self.lomitoPollo.isChecked():
            total = 450
        elif self.lomitoCerdo.isChecked():
            total = 400
        else:
            total = 0

        if self.huevoFrito.isChecked():
            total += 100
        if self.papasFritas.isChecked():
            total += 200
        if self.gaseosa.isChecked():
            total += 250
        if self.delivery.isChecked():
            total += 100

        self.precioTotal.setText(f"Precio total: ${total}")

app = QApplication([])
window = MiVentana()

window.show()
app.exec()