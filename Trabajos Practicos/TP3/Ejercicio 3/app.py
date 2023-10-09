from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ejercicio 3/MainWindow.ui", self)
        self.btnMostrar.clicked.connect(self.on_mostrar)
    
    def on_mostrar(self):
        nomCompleto = f"{self.fldApellido.text()}, {self.fldNombre.text()}"
        self.nombreCompleto.setText(nomCompleto)

app = QApplication([])
windows = MiVentana()
windows.show()

app.exec()