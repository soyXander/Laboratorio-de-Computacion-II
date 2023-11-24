from PyQt6.QtWidgets import QApplication, QComboBox, QDialog, QDialogButtonBox, QFileDialog, QHeaderView, QLabel, QLineEdit, QMainWindow, QMessageBox, QTableWidgetItem, QVBoxLayout, QWidget 
from PyQt6.QtCore import QRect
from PyQt6 import uic
from classes.Cancha import *
from classes.Cliente import *
from classes.Reserva import *
from utils import *
import csv

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(uiDir() + "mainWindow.ui", self)
        self.canchas = []
        self.reservas = []
        self.clientes = []
        
        self.tablaReservas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tablaClientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.cat = CatDancer()
        self.cat.init()
        self.gridLayout_6.addWidget(self.cat)
        
        # Señales de los botones
        self.btnInicio.clicked.connect(self.menuControl)
        
        self.btnCanchas.clicked.connect(self.menuControl)
        self.btnCrearCancha.clicked.connect(self.crearCancha)
        self.btnEditarCancha.clicked.connect(self.editarCancha)
        self.btnEliminarCancha.clicked.connect(self.eliminarCancha)
        
        self.btnClientes.clicked.connect(self.menuControl)
        self.btnCrearCliente.clicked.connect(self.crearCliente)
        self.btnEditarCliente.clicked.connect(self.editarCliente)
        self.btnEliminarCliente.clicked.connect(self.eliminarCliente)
    
        self.btnReservas.clicked.connect(self.menuControl)
        self.btnRespaldo.clicked.connect(self.menuControl)
        self.btnAcercaDe.clicked.connect(self.menuControl)
    
        self.btnCrearReserva.clicked.connect(self.crearReserva)
        self.btnEditarReserva.clicked.connect(self.editarReserva)
        self.btnCancelarReserva.clicked.connect(self.cancelarReserva)
        
        self.btnCargarRespaldo.clicked.connect(self.cargarRespaldo)
        self.btnDescargarRespaldo.clicked.connect(self.descargarRespaldo)

    # Canchas
    def crearCancha(self):
        ventana = CanchaDialog()
        ventana.setWindowTitle("Crear cancha")
        
        resultado = ventana.exec()
        if resultado == QDialog.DialogCode.Accepted:
            nombre = ventana.nombre.text()
            precio = ventana.precio.value()
            piso = ventana.piso.currentText()
            portada = ventana.portada.text()
            if ventana.tipo.currentText() == "Futbol 5":
                cancha = CanchaFutbol5(nombre, precio, piso, True, portada)
            elif ventana.tipo.currentText() == "Futbol 11":
                cancha = CanchaFutbol11(nombre, precio, piso, True, portada)
            elif ventana.tipo.currentText() == "Basquet":
                cancha = CanchaBasquet(nombre, precio, piso, True, portada)
            elif ventana.tipo.currentText() == "Padel":
                cancha = CanchaPadel(nombre, precio, piso, True, portada)

            self.canchas.append(cancha)
            self.actualizarCanchas()
    
    def editarCancha(self):
        # if len(self.canchas) == 0
        if not self.canchas:
            QMessageBox().warning(self, "Error", "No hay canchas disponibles")
            return
        
        msg = QDialog()
        msg.setWindowTitle("Editar cancha")
        msg.setWindowIcon(QIcon(imgDir() + "icon.png"))
        mensaje = QLabel("Selecciona la cancha que deseas editar", msg)
        cancha = QComboBox(msg)
        cancha.addItems([cancha.nombre for cancha in self.canchas])
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.button(QDialogButtonBox.StandardButton.Ok).setText("Editar")
        botones.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        
        # Señales de los botones
        botones.accepted.connect(msg.accept)
        botones.rejected.connect(msg.reject)
        
        layout = QVBoxLayout(msg)
        layout.addWidget(mensaje)
        layout.addWidget(cancha)
        layout.addWidget(botones)

        if msg.exec() == QDialog.DialogCode.Accepted:
            indice = cancha.currentIndex()
            
            ventana = CanchaDialog()
            ventana.setWindowTitle("Editar cancha")
            ventana.botones.button(QDialogButtonBox.StandardButton.Ok).setText("Editar")
            ventana.nombre.setText(self.canchas[indice].nombre)
            ventana.tipo.setCurrentText(self.canchas[indice].tipo)
            ventana.precio.setValue(float(self.canchas[indice].precio))
            ventana.piso.setCurrentText(self.canchas[indice].piso)
            ventana.portada.setText(self.canchas[indice].portada)
            if ventana.exec() == QDialog.DialogCode.Accepted:
                nombre = ventana.nombre.text()
                precio = ventana.precio.value() 
                piso = ventana.piso.currentText()
                portada = ventana.portada.text()
                if ventana.tipo.currentText() == "Futbol 5":
                    canchaActualizada = CanchaFutbol5(nombre, precio, piso, True, portada)
                elif ventana.tipo.currentText() == "Futbol 11":
                    canchaActualizada = CanchaFutbol11(nombre, precio, piso, True, portada)
                elif ventana.tipo.currentText() == "Basquet":
                    canchaActualizada = CanchaBasquet(nombre, precio, piso, True, portada)
                elif ventana.tipo.currentText() == "Padel":
                    canchaActualizada = CanchaPadel(nombre, precio, piso, True, portada)
                self.canchas[indice] = canchaActualizada
                self.actualizarCanchas()

    def eliminarCancha(self):
        if not self.canchas:
            QMessageBox().warning(self, "Error", "No hay canchas disponibles")
            return
        
        ventana = QDialog()
        ventana.setWindowTitle("Eliminar cancha")
        ventana.setWindowIcon(QIcon(imgDir() + "icon.png"))
        mensaje = QLabel("Selecciona la cancha que deseas eliminar", ventana)
        cancha = QComboBox(ventana)
        cancha.addItems([cancha.nombre for cancha in self.canchas])
        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.button(QDialogButtonBox.StandardButton.Ok).setText("Eliminar")
        botones.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        
        # Señales de los botones
        botones.accepted.connect(ventana.accept)
        botones.rejected.connect(ventana.reject)
        
        layout = QVBoxLayout(ventana)
        layout.addWidget(mensaje)
        layout.addWidget(cancha)
        layout.addWidget(botones)
        
        if ventana.exec() == QDialog.DialogCode.Accepted:
            indice = cancha.currentIndex()
            msg = QMessageBox()
            msg.setWindowTitle("Eliminar")
            msg.setWindowIcon(QIcon(imgDir() + "icon.png"))
            msg.setText(f"¿Deseas eliminar la cancha {self.canchas[indice].nombre}?")
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.button(QMessageBox.StandardButton.Yes).setText("Si")
            if msg.exec() == QMessageBox.StandardButton.Yes:
                self.canchas.pop(indice)
                self.actualizarCanchas()

    def actualizarCanchas(self):
        for children in self.listaCanchas.findChildren(QWidget):
            children.deleteLater()
        
        for i in range(len(self.canchas)):
            tarjeta = CrearTarjetaCancha(self.canchas[i])
            self.gridLayout_9.addWidget(tarjeta, i // 3, i % 3)

    # Clientes
    def crearCliente(self):
        ventana = ClienteDialog()
        ventana.setWindowTitle("Crear cliente")
        
        if ventana.exec() == QDialog.DialogCode.Accepted:
            nombre = ventana.nombre.text()
            apellido = ventana.apellido.text()
            telefono = ventana.telefono.text()
            email = ventana.email.text()
            
            cliente = Cliente(nombre, apellido, telefono, email)
            
            self.clientes.append(cliente)
            self.actualizarTablaClientes()
        
    def editarCliente(self):
        if not self.clientes:
            QMessageBox().warning(self, "Error", "No hay clientes disponibles")
            return
        
        self.item = self.tablaClientes.currentItem()
        
        if not self.item:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningun cliente")
            return
        
        fila = self.item.row()
        nombre_text = self.tablaClientes.item(fila, 0).text()
        apellido_text = self.tablaClientes.item(fila, 1).text()
        telefono_text = self.tablaClientes.item(fila, 2).text()
        email_text = self.tablaClientes.item(fila, 3).text()
        
        ventana = ClienteDialog()
        ventana.setWindowTitle("Editar cliente")
        ventana.botones.button(QDialogButtonBox.StandardButton.Ok).setText("Editar")
        ventana.nombre.setText(nombre_text)
        ventana.apellido.setText(apellido_text)
        ventana.telefono.setText(telefono_text)
        ventana.email.setText(email_text)
        
        if ventana.exec() == QDialog.DialogCode.Accepted:
            nombre = ventana.nombre.text()
            apellido = ventana.apellido.text()
            telefono = ventana.telefono.text()
            email = ventana.email.text()
            
            cliente = Cliente(nombre, apellido, telefono, email)
            self.clientes[fila] = cliente
            self.actualizarTablaClientes()
    
    def eliminarCliente(self):
        if not self.clientes:
            QMessageBox().warning(self, "Error", "No hay clientes disponibles")
            return
        
        self.item = self.tablaClientes.currentItem()
        
        if not self.item:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningun cliente")
            return
        
        fila = self.item.row()
        msg = QMessageBox()
        msg.setWindowTitle("Eliminar")
        msg.setWindowIcon(QIcon(imgDir() + "icon.png"))
        msg.setText(f"¿Deseas eliminar el cliente {self.clientes[fila].apellido} {self.clientes[fila].apellido}?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.button(QMessageBox.StandardButton.Yes).setText("Si")
        if msg.exec() == QMessageBox.StandardButton.Yes:
            self.clientes.pop(fila)
            self.actualizarTablaClientes()
            
    def actualizarTablaClientes(self):
        self.tablaClientes.setRowCount(0)
        
        for cliente in self.clientes:
            fila = self.tablaClientes.rowCount()
            self.tablaClientes.insertRow(fila)
            self.tablaClientes.setItem(fila, 0, QTableWidgetItem(cliente.apellido))
            self.tablaClientes.setItem(fila, 1, QTableWidgetItem(cliente.nombre))
            self.tablaClientes.setItem(fila, 2, QTableWidgetItem(cliente.telefono))
            self.tablaClientes.setItem(fila, 3, QTableWidgetItem(cliente.email))
    
    # Reservas
    def crearReserva(self):
        if not self.canchas:
            QMessageBox().warning(self, "Error", "No hay canchas disponibles")
            return
        
        ventana = ReservaDialog()
        ventana.setWindowTitle("Crear reserva")
        ventana.cliente.addItems([f"{cliente.apellido}, {cliente.nombre}" for cliente in self.clientes])
        ventana.cliente.setCurrentIndex(-1)
        ventana.cancha.addItems([cancha.nombre for cancha in self.canchas])
        ventana.cancha.setCurrentIndex(-1)
        
        ventana.cancha.currentIndexChanged.connect(lambda: ventana.costo.setText(str(self.canchas[ventana.cancha.currentIndex()].precio)))
        ventana.crearCliente.clicked.connect(self.crearCliente)
        ventana.crearCliente.clicked.connect(lambda: ventana.limpiarClientes())
        ventana.crearCliente.clicked.connect(lambda: ventana.cliente.addItems([f"{cliente.apellido}, {cliente.nombre}" for cliente in self.clientes]))
        ventana.crearCliente.clicked.connect(lambda: ventana.cliente.setCurrentIndex(-1))
        
        if ventana.exec() == QDialog.DialogCode.Accepted:
            cliente = ventana.cliente.currentText()
            cancha = ventana.cancha.currentText()
            costo = ventana.costo.text()
            fecha = ventana.fecha.text()
            hora = ventana.hora.currentText()
            
            # Validación de reserva
            if not self.reservaDisponible(cancha, fecha, hora):
                QMessageBox().warning(self, "Error", "La cancha ya esta reservada")
                return
            
            msg = QMessageBox()
            msg.setWindowTitle("Reservar")
            msg.setWindowIcon(QIcon(imgDir() + "icon.png"))
            msg.setText(f"¿Deseas reservar la cancha {cancha} para el cliente {cliente} el dia {fecha} a las {hora} por ${costo}?")
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if msg.exec() == QMessageBox.StandardButton.No:
                return
            
            reserva = Reserva(cliente, cancha, costo, fecha, hora)
            self.reservas.append(reserva)
            self.actualizarTablaReservas()

    def editarReserva(self):
        if not self.reservas:
            QMessageBox().warning(self, "Error", "No hay reservas disponibles")
            return
        
        self.item = self.tablaReservas.currentItem()
        
        if not self.item:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ninguna reserva")
            return

        fila = self.item.row()
        cliente_text = self.tablaReservas.item(fila, 0).text()
        cancha_text = self.tablaReservas.item(fila, 1).text()
        costo_text = self.tablaReservas.item(fila, 2).text()
        fecha_text = self.tablaReservas.item(fila, 3).text()
        hora_text = self.tablaReservas.item(fila, 4).text()
        
        ventana = ReservaDialog()
        ventana.setWindowTitle("Editar reserva")
        ventana.botones.button(QDialogButtonBox.StandardButton.Ok).setText("Editar")
        ventana.cliente.addItems([f"{cliente.apellido}, {cliente.nombre}" for cliente in self.clientes])
        ventana.cliente.setCurrentText(cliente_text)
        ventana.cancha.addItems([cancha.nombre for cancha in self.canchas])
        ventana.cancha.setCurrentText(cancha_text)
        ventana.cancha.currentIndexChanged.connect(lambda: ventana.costo.setText(str(self.canchas[ventana.cancha.currentIndex()].precio)))
        ventana.costo.setText(costo_text)
        ventana.fecha.setDate(QDate.fromString(fecha_text, "dd/MM/yyyy"))
        ventana.hora.setCurrentText(hora_text)
        
        if ventana.exec() == QDialog.DialogCode.Accepted:
            cliente = ventana.cliente.currentText()
            cancha = ventana.cancha.currentText()
            costo = ventana.costo.text()
            fecha = ventana.fecha.text()
            hora = ventana.hora.currentText()
            
            # Validación de reserva
            if not self.reservaDisponible(cancha, fecha, hora):
                QMessageBox().warning(self, "Error", "La cancha ya esta reservada")
                return
            
            reserva = Reserva(cliente, cancha, costo, fecha, hora)
            self.reservas[fila] = reserva
            self.actualizarTablaReservas()
   
    def cancelarReserva(self):
        if not self.reservas:
            QMessageBox().warning(self, "Error", "No hay reservas disponibles")
            return
        
        self.item = self.tablaReservas.currentItem()
        
        if not self.item:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ninguna reserva")
            return
        
        fila = self.item.row()
        cliente = self.tablaReservas.item(fila, 0).text()
        cancha = self.tablaReservas.item(fila, 1).text()
        fecha = self.tablaReservas.item(fila, 2).text()
        hora = self.tablaReservas.item(fila, 3).text()
        
        msg = QMessageBox()
        msg.setWindowTitle("Cancelar")
        msg.setWindowIcon(QIcon(imgDir() + "icon.png"))
        msg.setText(f"¿Deseas cancelar la reserva de {cliente} en la cancha {cancha} en la fecha del {fecha} a las {hora}?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.button(QMessageBox.StandardButton.Yes).setText("Si")
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            self.reservas.pop(fila)
            self.actualizarTablaReservas()

    def reservaDisponible(self, cancha, fecha, horario):
        for reserva in self.reservas:
            if reserva.cancha == cancha and reserva.fecha == fecha and reserva.hora == horario:
                return False
        return True

    def actualizarTablaReservas(self):
        self.tablaReservas.setRowCount(0)
        # Ordenar por fecha y luego por hora
        self.reservas.sort(key=lambda reserva: (reserva.fecha, reserva.hora))
        
        for reserva in self.reservas:
            fila = self.tablaReservas.rowCount()
            self.tablaReservas.insertRow(fila)
            self.tablaReservas.setItem(fila, 0, QTableWidgetItem(reserva.cliente))
            self.tablaReservas.setItem(fila, 1, QTableWidgetItem(reserva.cancha))
            self.tablaReservas.setItem(fila, 2, QTableWidgetItem(reserva.costo))
            self.tablaReservas.setItem(fila, 3, QTableWidgetItem(reserva.fecha))
            self.tablaReservas.setItem(fila, 4, QTableWidgetItem(reserva.hora))

    # Respaldo
    def cargarRespaldo(self):
        archivo, ok = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            backupDir(),
            "Archivos de texto (*.csv)"
        )
        if ok:
            with open(archivo) as archivo:
                filas = csv.reader(archivo, delimiter=",", quotechar="\"")
                for fila in filas:
                    if fila[0] == "cancha":
                        cancha = 0
                        if fila[2].casefold() == "Futbol 5".casefold():
                            cancha = CanchaFutbol5(fila[1], fila[3], fila[4], fila[5], fila[6])
                        elif fila[2].casefold() == "Futbol 11".casefold():
                            cancha = CanchaFutbol11(fila[1], fila[3], fila[4], fila[5], fila[6])
                        elif fila[2].casefold() == "Basquet".casefold():
                            cancha = CanchaBasquet(fila[1], fila[3], fila[4], fila[5], fila[6])
                        elif fila[2].casefold() == "Padel".casefold():
                            cancha = CanchaPadel(fila[1], fila[3], fila[4], fila[5], fila[6])
                        self.canchas.append(cancha)
                    elif fila[0] == "cliente":
                        cliente = Cliente(fila[1], fila[2], fila[3], fila[4])
                        self.clientes.append(cliente)
                    elif fila[0] == "reserva":
                        reserva = Reserva(fila[1], fila[2], fila[3], fila[4], fila[5])
                        self.reservas.append(reserva)
            #archivo.close()
            self.actualizarCanchas()
            self.actualizarTablaReservas()
            QMessageBox().information(self, "Información", "Respaldo cargado correctamente")

    def descargarRespaldo(self):
        archivo, ok = QFileDialog.getSaveFileName(
            self,
            "Seleccionar archivo",
            backupDir(),
            "Archivos de texto (*.csv)"
        )
        if ok:
            with open(archivo, "w", newline="") as archivo:
                escritor = csv.writer(archivo, delimiter=",", quotechar="\"", quoting=csv.QUOTE_NONNUMERIC)
                for cancha in self.canchas:
                    escritor.writerow(["cancha", cancha.nombre, cancha.tipo, cancha.precio, cancha.piso, cancha.abierta, cancha.portada])
                for cliente in self.clientes:
                    escritor.writerow(["cliente", cliente.nombre, cliente.apellido, cliente.telefono, cliente.email])
                for reserva in self.reservas:
                    escritor.writerow(["reserva", reserva.cliente, reserva.cancha, reserva.costo, reserva.fecha, reserva.hora])
            #archivo.close()
            msg = QMessageBox()
            msg.setText("Respaldo descargado correctamente")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Informacion")
            msg.exec()

    # Menu control
    def menuControl(self):
        señal = self.sender()
        if señal == self.btnCanchas:
            self.stackedWidget.setCurrentIndex(1)
            self.actualizarCanchas()
        elif señal == self.btnReservas:
            self.stackedWidget.setCurrentIndex(2)
            self.actualizarTablaReservas()
        elif señal == self.btnClientes:
            self.stackedWidget.setCurrentIndex(3)
            self.actualizarTablaClientes()
        elif señal == self.btnRespaldo:
            self.stackedWidget.setCurrentIndex(4)
        elif señal == self.btnAcercaDe:
            self.stackedWidget.setCurrentIndex(5)
        else:
            self.stackedWidget.setCurrentIndex(0)

app = QApplication([])
window = MiVentana()

window.show()
app.exec()