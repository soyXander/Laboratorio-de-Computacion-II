from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6 import uic
import os

class Persona():
  def __init__(self, nombre, apellido, email):
    self.nombre = nombre
    self.apellido = apellido
    self.email = email
  
  def __str__(self):
    return f"{self.apellido}, {self.nombre}, {self.email}"

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "mainWindow.ui"), self)
        self.btnAgregar.clicked.connect(self.on_agregar)
        self.btnEditar.clicked.connect(self.on_editar)
        self.btnEliminar.clicked.connect(self.on_eliminar)
        self.btnGuardar.clicked.connect(self.on_guardar)
        self.btnCancelar.clicked.connect(self.on_cancelar)

    def on_agregar(self):
        nombre = self.nombreInput.text()
        apellido = self.apellidoInput.text()
        email = self.emailInput.text()
        
        persona = Persona(nombre, apellido, email)

        if len(nombre) > 0 or len(apellido) > 0 or len(email) > 0:
            fila = self.tabla.rowCount()
            self.tabla.insertRow(fila)
            self.tabla.setItem(fila, 0, QTableWidgetItem(persona.nombre))
            self.tabla.setItem(fila, 1, QTableWidgetItem(persona.apellido))
            self.tabla.setItem(fila, 2, QTableWidgetItem(persona.email))
            
            self.limpiarCampos()
            
    def on_editar(self):
        self.item = self.tabla.currentItem()
        
        if not self.item:
            return
        
        self.showBtns()
        
        fila = self.item.row()
        nombre = self.tabla.item(fila, 0).text()
        apellido = self.tabla.item(fila, 1).text()
        email = self.tabla.item(fila, 2).text()
        
        self.nombreInput.setText(nombre)
        self.apellidoInput.setText(apellido)
        self.emailInput.setText(email)

    def on_eliminar(self):
        item = self.tabla.currentItem()
        
        if not item:
            return
        
        dialog = QMessageBox()
        dialog.setWindowTitle("Confirmar eliminación")
        dialog.setIcon(QMessageBox.Icon.Warning)
        dialog.setText("¿Desea eliminar la persona? Este proceso no se puede deshacer")  
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)      
        
        if dialog.exec() == QMessageBox.StandardButton.Yes:
            fila = item.row()
            self.tabla.removeRow(fila)
        
            self.limpiarCampos()

    def on_guardar(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Confirmar edición")
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setText("¿Desea guardar los cambios?")
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if dialog.exec() == QMessageBox.StandardButton.Yes:
            nombre = self.nombreInput.text()
            apellido = self.apellidoInput.text()
            email = self.emailInput.text()

            persona = Persona(nombre, apellido, email)
            
            if len(persona.nombre) > 0 or len(persona.apellido) > 0 or len(persona.email) > 0:
                fila = self.item.row()
                self.tabla.setItem(fila, 0, QTableWidgetItem(persona.nombre))
                self.tabla.setItem(fila, 1, QTableWidgetItem(persona.apellido))
                self.tabla.setItem(fila, 2, QTableWidgetItem(persona.email))

            self.showBtns()
            self.limpiarCampos()
        
    def on_cancelar(self):
        self.showBtns()
        self.limpiarCampos()

    def limpiarCampos(self):
        self.nombreInput.setText("")
        self.apellidoInput.setText("")
        self.emailInput.setText("")

    def showBtns(self):
        self.wgBotones.setVisible(not self.wgBotones.isVisible())
        self.btnGuardar.setVisible(self.wgBotones.isVisible())
        self.btnCancelar.setVisible(self.wgBotones.isVisible())
        self.btnAgregar.setEnabled(not self.wgBotones.isVisible())
        self.btnEditar.setEnabled(not self.wgBotones.isVisible())
        self.btnEliminar.setEnabled(not self.wgBotones.isVisible())

app = QApplication([])
window = MiVentana()

window.show()
app.exec()