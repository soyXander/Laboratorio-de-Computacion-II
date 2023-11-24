from PyQt6.QtCore import QDate, QTime
from PyQt6.QtWidgets import QComboBox, QDateEdit, QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QMessageBox, QPushButton, QTimeEdit
from classes.Cliente import *

class Reserva:
    def __init__(self, cliente, cancha, costo, fecha, hora):
        self.cliente = cliente
        self.cancha = cancha
        self.costo = costo
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"Reserva: {self.cliente} - {self.cancha} - {self.costo} - {self.fecha} - {self.hora}"
class ReservaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(imgDir() + "icon.png"))
        
        self.cliente = QComboBox(self)
        self.crearCliente = QPushButton("Crear cliente", self)
        self.cancha = QComboBox(self)
        self.costo = QLineEdit(self)
        self.costo.setReadOnly(True)
        
        self.hora = QComboBox(self)
        self.hora.addItems(["00:00", "01:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00","21:00", "22:00", "23:00"])
        
        self.fecha = QDateEdit(self)
        self.fecha.setCalendarPopup(True)
        self.fecha.setDisplayFormat("yyyy-MM-dd")
        self.fecha.setDate(QDate.currentDate())
        
        self.botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        self.botones.button(QDialogButtonBox.StandardButton.Ok).setText("Reservar")
        self.botones.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        
        # Construccion del layout
        layout = QFormLayout(self)
        layout.addRow("Cliente", self.cliente)
        layout.addRow("", self.crearCliente)
        layout.addRow("Cancha", self.cancha)
        layout.addRow("Costo", self.costo)
        layout.addRow("Fecha", self.fecha)
        layout.addRow("Hora", self.hora)
        layout.addRow(self.botones)
        
        # Señales de los botones
        self.botones.accepted.connect(self.accept)
        self.botones.rejected.connect(self.reject)
        
        # Validar campos
        self.validar()
        
        # Señales para validar campos
        self.cliente.currentIndexChanged.connect(self.validar)
        self.cancha.currentIndexChanged.connect(self.validar)
        
    def validar(self):
        self.botones.button(QDialogButtonBox.StandardButton.Ok).setEnabled(
            bool(self.cliente.currentIndex() > -1 and self.cancha.currentIndex() > -1))
        self.cliente.setStyleSheet("border: 1px solid red" if self.cliente.currentIndex() == -1 else "")
        self.cancha.setStyleSheet("border: 1px solid red" if self.cancha.currentIndex() == -1 else "")
    
    # Metodo para limpiar los clientes en el comboBox
    def limpiarClientes(self):
        self.cliente.clear()