from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnCambiar.clicked.connect(self.on_cambiar_saludo)
    
    def on_cambiar_saludo(self):
        if self.mensaje.text() == "Hola Mundo!":
            self.mensaje.setText("Chau Mundo!")
        else:
            self.mensaje.setText("Hola Mundo!")

app = QApplication([])
window = MiVentana()

window.show()
app.exec()