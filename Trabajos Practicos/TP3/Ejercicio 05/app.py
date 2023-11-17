from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnCalcular.clicked.connect(self.on_calcular)

    def on_calcular(self):
        temp = self.tempIn.text()
        if temp.isdigit():
            temp = float(temp)
        else:
            self.tempIn.setText("")
            return
        
        if self.cenKel.isChecked():
            temp = temp + 273.15
        elif self.kelCen.isChecked():
            temp = temp - 273.15
        elif self.cenFah.isChecked():
            temp = (temp * 9 / 5) + 32
        elif self.fahCen.isChecked():
            temp = (temp - 32) * 5 / 9
        
        self.labelTemp.setText(f"Temperatura: {temp:.2f}")

app = QApplication([])
window = MiVentana()

window.show()
app.exec()