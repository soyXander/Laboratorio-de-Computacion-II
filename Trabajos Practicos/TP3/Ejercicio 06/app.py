from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import os

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnMostrar.clicked.connect(self.on_mostrar)
        
    def on_mostrar(self):
        msg = QMessageBox()
        msg.setWindowTitle(self.titulo.text())
        msg.setText(self.mensaje.text())
        
        if self.rbInformacion.isChecked():
            msg.setIcon(QMessageBox.Icon.Information)
        elif self.rbPregunta.isChecked():
            msg.setIcon(QMessageBox.Icon.Question)
        elif self.rbPrecaucion.isChecked():
            msg.setIcon(QMessageBox.Icon.Warning)
        elif self.rbCritico.isChecked():
            msg.setIcon(QMessageBox.Icon.Critical)
        
        botones = QMessageBox.StandardButton.NoButton
        if self.chSi.isChecked():
            botones |= QMessageBox.StandardButton.Yes
        if self.chNo.isChecked():
            botones |= QMessageBox.StandardButton.No
        if self.chCancelar.isChecked():
            botones |= QMessageBox.StandardButton.Cancel
        if self.chOk.isChecked():
            botones |= QMessageBox.StandardButton.Ok
        if self.chAbrir.isChecked():
            botones |= QMessageBox.StandardButton.Open
        if self.chCerrar.isChecked():
            botones |= QMessageBox.StandardButton.Close
        if self.chGuardar.isChecked():
            botones |= QMessageBox.StandardButton.Save
        if self.chGuardarTodo.isChecked():
            botones |= QMessageBox.StandardButton.SaveAll
        if self.chAbortar.isChecked():
            botones |= QMessageBox.StandardButton.Abort
        if self.chReintentar.isChecked():
            botones |= QMessageBox.StandardButton.Retry
        if self.chIgnorar.isChecked():
            botones |= QMessageBox.StandardButton.Ignore
        
        msg.setStandardButtons(botones)
        msg.exec()

app = QApplication([])
window = MiVentana()

window.show()
app.exec()