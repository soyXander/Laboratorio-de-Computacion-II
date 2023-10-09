from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ejercicio 1/MainWindow.ui", self)
        self.btnCambiar.clicked.connect(self.on_cambiar_saludo)
    
    def on_cambiar_saludo(self):
        self.mensaje.setText("Chau Mundo!")

app = QApplication([])
windows = MiVentana()
windows.show()

app.exec()