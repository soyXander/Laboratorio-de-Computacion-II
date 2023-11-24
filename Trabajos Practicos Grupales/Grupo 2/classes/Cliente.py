from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit
from PyQt6.QtGui import QIcon
from utils import imgDir

class Cliente:
    def __init__(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.historial = []
        
    def __str__(self):
        return f"{self.apellido}, {self.nombre}  - {self.telefono} - {self.email}"
    
class ClienteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(imgDir() + "icon.png"))
        
        self.apellido = QLineEdit(self)
        self.nombre = QLineEdit(self)
        self.telefono = QLineEdit(self)
        self.email = QLineEdit(self)

        self.botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        self.botones.button(QDialogButtonBox.StandardButton.Ok).setText("Crear")
        self.botones.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        
        # Construccion del layout
        layout = QFormLayout(self)
        layout.addRow("Apellido", self.apellido)
        layout.addRow("Nombre", self.nombre)
        layout.addRow("Telefono", self.telefono)
        layout.addRow("Email", self.email)
        layout.addRow(self.botones)
        
        # Señales de los botones
        self.botones.accepted.connect(self.accept)
        self.botones.rejected.connect(self.reject)
        
        # Validar campos
        self.validar()
        
        # Señales para validar campos
        self.apellido.textChanged.connect(self.validar)
        self.nombre.textChanged.connect(self.validar)
        self.telefono.textChanged.connect(self.validar)
        self.email.textChanged.connect(self.validar)
        
    def validar(self):
        self.botones.button(QDialogButtonBox.StandardButton.Ok).setEnabled(
            bool(self.apellido.text())
            and bool(self.nombre.text())
            and self.telefono.text().isnumeric()
            and self.email.text().count("@") == 1
        )
        self.nombre.setStyleSheet("border: 1px solid red;" if not bool(self.nombre.text()) else "")
        self.apellido.setStyleSheet("border: 1px solid red;" if not bool(self.apellido.text()) else "")
        self.telefono.setStyleSheet("border: 1px solid red;" if not bool(self.telefono.text()) and self.telefono.text().isnumeric() else "")
        self.email.setStyleSheet("border: 1px solid red;" if not bool(self.email.text()) else "")
        
        # if not self.email.text().count("@") > 1:
        #     self.email.setStyleSheet("border: 1px solid red;")