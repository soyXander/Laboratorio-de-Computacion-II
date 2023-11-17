from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6 import uic
import csv, os

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
        self.btnCSV.clicked.connect(self.on_csv)
        self.btnCargarCSV.clicked.connect(self.on_cargarCSV)
        self.btnDescargarCSV.clicked.connect(self.on_descargarCSV)

    def on_agregar(self):
        if self.btnGuardar.isVisible():
            self.showBtns(1)
        
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
        
        self.showBtns(1)
        
        fila = self.item.row()
        nombre = self.tabla.item(fila, 0).text()
        apellido = self.tabla.item(fila, 1).text()
        email = self.tabla.item(fila, 2).text()
        
        self.nombreInput.setText(nombre)
        self.apellidoInput.setText(apellido)
        self.emailInput.setText(email)

    def on_eliminar(self):
        if self.btnGuardar.isVisible():
            self.showBtns(2)
        
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

            self.showBtns(1)
            self.limpiarCampos()
        
    def on_cancelar(self):
        self.showBtns(1)
        self.limpiarCampos()

    def on_csv(self):
        self.showBtns(2)

    def on_cargarCSV(self):
        archivoSubido, ok = QFileDialog.getOpenFileName(
            self,
            "Cargar archivo CSV",
            os.path.dirname(__file__),
            "Archivo CSV (*.csv)"
        )
        if ok:
            with open(archivoSubido) as archivoSubido:
                filas = csv.reader(archivoSubido, delimiter=",", quotechar="\"")
                for filaCSV in filas:
                    persona = Persona(filaCSV[0], filaCSV[1], filaCSV[2])
                    
                    if len(persona.nombre) > 0 or len(persona.apellido) > 0 or len(persona.email) > 0:
                        fila = self.tabla.rowCount()
                        self.tabla.insertRow(fila)
                        self.tabla.setItem(fila, 0, QTableWidgetItem(persona.nombre))
                        self.tabla.setItem(fila, 1, QTableWidgetItem(persona.apellido))
                        self.tabla.setItem(fila, 2, QTableWidgetItem(persona.email))
            archivoSubido.close()
            self.showBtns(2)

    def on_descargarCSV(self):
        if self.tabla.rowCount() > 0:
            archivoDescargado, ok = QFileDialog.getSaveFileName(
                self,
                "Guardar archivo CSV",
                os.path.dirname(__file__),
                "Archivo CSV (*.csv)"
            )
            if ok:
                with open(archivoDescargado, "w", newline="") as archivoDescargado:
                    escritor = csv.writer(archivoDescargado, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
                    for fila in range(self.tabla.rowCount()):
                        nombre = self.tabla.item(fila, 0).text()
                        apellido = self.tabla.item(fila, 1).text()
                        email = self.tabla.item(fila, 2).text()
                        escritor.writerow([nombre, apellido, email])
                archivoDescargado.close()
                self.showBtns(2)

    def limpiarCampos(self):
        self.nombreInput.setText("")
        self.apellidoInput.setText("")
        self.emailInput.setText("")

    def showBtns(self, opc):
        if opc == 1:
            self.wgBotones.setVisible(not self.wgBotones.isVisible())
            self.btnGuardar.setVisible(self.wgBotones.isVisible())
            self.btnCancelar.setVisible(self.wgBotones.isVisible())
            self.btnAgregar.setEnabled(not self.wgBotones.isVisible())
            self.btnEditar.setEnabled(not self.wgBotones.isVisible())
            self.btnEliminar.setEnabled(not self.wgBotones.isVisible())
            self.btnCSV.setEnabled(not self.wgBotones.isVisible())
        elif opc == 2:
            self.wgBotones.setVisible(not self.wgBotones.isVisible())
            self.nombreInput.setEnabled(not self.wgBotones.isVisible())
            self.apellidoInput.setEnabled(not self.wgBotones.isVisible())
            self.emailInput.setEnabled(not self.wgBotones.isVisible())
            self.btnCargarCSV.setVisible(self.wgBotones.isVisible())
            self.btnDescargarCSV.setVisible(self.wgBotones.isVisible())
            self.btnAgregar.setEnabled(not self.wgBotones.isVisible())
            self.btnEditar.setEnabled(not self.wgBotones.isVisible())
            self.btnEliminar.setEnabled(not self.wgBotones.isVisible())

app = QApplication([])
window = MiVentana()

window.show()
app.exec()