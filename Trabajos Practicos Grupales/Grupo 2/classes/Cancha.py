from PyQt6.QtWidgets import QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFormLayout, QGroupBox, QLineEdit, QLabel, QPushButton, QDoubleSpinBox, QVBoxLayout 
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap
import os
from utils import imgDir

class Cancha:
    def __init__(self, nombre, precio, piso, abierta, portada = "default.jpg"):
        self.nombre = nombre
        self.precio = precio
        self.piso = piso
        self.abierta = abierta
        self.libre = True
        self.portada = portada
    
class CanchaFutbol5(Cancha):
    def __init__(self, nombre, precio, piso, abierta, portada):
        super().__init__(nombre, precio, piso, abierta, portada)
        self.tipo = "Futbol 5"
    
    def __str__(self):
        return f"Cancha {self.nombre} - ${self.precio} - {self.piso} - {self.abierta} - {self.libre} - {self.tipo} - {self.portada}"

class CanchaFutbol11(Cancha):
    def __init__(self, nombre, precio, piso, abierta, portada):
        super().__init__(nombre, precio, piso, abierta, portada)
        self.tipo = "Futbol 11"
    
    def __str__(self):
        return f"Cancha {self.nombre} - ${self.precio} - {self.piso} - {self.abierta} - {self.libre} - {self.tipo} - {self.portada}"

class CanchaBasquet(Cancha):
    def __init__(self, nombre, precio, piso, abierta, portada):
        super().__init__(nombre, precio, piso, abierta, portada)
        self.tipo = "Basquet"
        
    def __str__(self):
        return f"Cancha {self.nombre} - ${self.precio} - {self.piso} - {self.abierta} - {self.libre} - {self.tipo} - {self.portada}"

class CanchaPadel(Cancha):
    def __init__(self, nombre, precio, piso, abierta, portada):
        super().__init__(nombre, precio, piso, abierta, portada)
        self.tipo = "Padel"
    
    def __str__(self):
        return f"Cancha {self.nombre} - ${self.precio} - {self.piso} - {self.abierta} - {self.libre} - {self.tipo} - {self.portada}"

class CanchaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(imgDir() + "icon.png"))
        
        self.nombre = QLineEdit(self)
        self.tipo = QComboBox(self)
        self.tipo.addItems(["Futbol 5", "Futbol 11", "Basquet", "Padel"])
        self.tipo.setCurrentIndex(-1)
        self.precio = QDoubleSpinBox(self)
        self.precio.setPrefix("$ ")
        self.precio.setRange(0, 1000000)
        self.piso = QComboBox(self)
        self.piso.addItems(["Cesped sintetico", "Cesped natural", "Cemento", "Parquet", "Goma", "Tierra"])
        self.piso.setCurrentIndex(-1)
        
        self.portada = QLineEdit(self)
        self.portada.setText("default.jpg")
        self.portada.setEnabled(False)
        self.btnPortada = QPushButton("Seleccionar portada", self)
        self.btnPortada.clicked.connect(self.seleccionarPortada)
        
        self.botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        self.botones.button(QDialogButtonBox.StandardButton.Ok).setText("Crear")
        self.botones.button(QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
        
        # Construccion del formulario
        layout = QFormLayout(self)
        layout.addRow("Nombre:", self.nombre)
        layout.addRow("Tipo de cancha:", self.tipo)
        layout.addRow("Precio:", self.precio)
        layout.addRow("Tipo de suelo:", self.piso)
        layout.addRow("Portada:", self.portada)
        layout.addRow(self.btnPortada)
        layout.addRow(self.botones)
        
        # Señales de los botones
        self.botones.accepted.connect(self.accept)
        self.botones.rejected.connect(self.reject)

        # Validar campos
        self.validar()
        
        # Señales para validar campos
        self.nombre.textChanged.connect(self.validar)
        self.tipo.currentIndexChanged.connect(self.validar)
        self.piso.currentIndexChanged.connect(self.validar)
        
    def seleccionarPortada(self):
        archivo, ok = QFileDialog.getOpenFileName(
            self,
            "Seleccionar portada",
            imgDir() + "img",
            "Imagenes (*.jpg *.png)")
        if ok:
            self.portada.setText(os.path.basename(archivo))

    def validar(self):
        self.botones.button(QDialogButtonBox.StandardButton.Ok).setEnabled(
            bool(self.nombre.text())
            and self.tipo.currentIndex() != -1
            and self.piso.currentIndex() != -1
        )
        
        # if not bool(self.nombre.text()):
        #     self.nombre.setStyleSheet("border: 1px solid red;")
        # else:
        #     self.nombre.setStyleSheet("")
        
        self.nombre.setStyleSheet("border: 1px solid red;" if not bool(self.nombre.text()) else "")
        self.tipo.setStyleSheet("border: 1px solid red;" if self.tipo.currentIndex() == -1 else "")
        self.piso.setStyleSheet("border: 1px solid red;" if self.piso.currentIndex() == -1 else "")

class CrearTarjetaCancha(QGroupBox):
    def __init__(self, cancha):
        super().__init__()
        self.setTitle(cancha.tipo)
        nombre = cancha.nombre.strip().replace(" ", "")
        self.setObjectName(u"cancha_" + nombre)
        self.setMaximumSize(QSize(180, 250))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo = QLabel(self)
        self.titulo.setObjectName(u"titulo")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.titulo.setText(cancha.nombre)
        self.titulo.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.titulo)

        self.precio = QLabel(self)
        self.precio.setObjectName(u"precio")
        self.precio.setText(f"$ {cancha.precio}")
        self.precio.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.precio)

        self.portada = QLabel(self)
        self.portada.setObjectName(u"portada")
        self.portada.setPixmap(QPixmap(imgDir() + cancha.portada))
        self.portada.setScaledContents(True)
        self.portada.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.portada.setMinimumSize(QSize(150, 150))
        self.portada.setMaximumSize(QSize(150, 150))

        self.verticalLayout.addWidget(self.portada)
        
        self.piso = QLabel(self)
        self.piso.setObjectName(u"piso")
        self.piso.setText(cancha.piso)
        self.piso.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.piso.setMaximumSize(QSize(16777215, 40))
        
        self.verticalLayout.addWidget(self.piso)
