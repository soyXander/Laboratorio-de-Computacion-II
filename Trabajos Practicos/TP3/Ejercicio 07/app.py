from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnAgregar.clicked.connect(self.on_agregar)
        self.btnEditar.clicked.connect(self.on_editar)
        self.btnQuitar.clicked.connect(self.on_quitar)
        self.btnQuitarTodo.clicked.connect(self.on_quitar_todo)
        
    def on_agregar(self):
        elem, ok = QInputDialog.getText(self, "Agregar elemento", "Introduce el nombre del nuevo elemento:")
        if ok:
            self.comboBox.addItem(elem)

    def on_editar(self):
        elem = self.comboBox.currentText()
        if elem:
            nuevoElem, ok = QInputDialog.getText(self, "Editar elemento", "Edita el nombre del elemento:", text=elem)
            if ok:
                index = self.comboBox.currentIndex()
                self.comboBox.setItemText(index, nuevoElem)

    def on_quitar(self):
        elem = self.comboBox.currentText()
        
        msg = QMessageBox()
        msg.setWindowTitle(f"Quitar elemento")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(f"¿Seguro que quiere quitar el elemento \"{elem}\"?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        signal = msg.exec()
        
        if signal == QMessageBox.StandardButton.Yes: 
            if elem:
                self.comboBox.removeItem(self.comboBox.currentIndex())

    def on_quitar_todo(self):
        msg = QMessageBox()
        msg.setWindowTitle(f"Quitar todos los elementos")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(f"¿Seguro que quiere quitar todos los elementos?")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        signal = msg.exec()
        
        if signal == QMessageBox.StandardButton.Yes: 
            self.comboBox.clear()
        
app = QApplication([])
window = MiVentana()

window.show()
app.exec()