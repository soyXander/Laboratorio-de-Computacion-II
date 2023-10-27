class Cancha:
    def __init__(self, id, precio):
        self.id = id
        self.libre = True
        self.precio = precio
        
class CanchaFutbol5(Cancha):
    def __init__(self, id, precio, tipoCesped, abierta):
        super().__init__(id, precio)
        self.tipoCesped = tipoCesped
        self.abierta = abierta

class CanchaFutbol11(Cancha):
    def __init__(self, id, precio, tipoCesped, abierta):
        super().__init__(id, precio)
        self.tipoCesped = tipoCesped
        self.abierta = abierta

class CanchaPadel(Cancha):
    def __init__(self, id, precio, tipoCesped, abierta):
        super().__init__(id, precio)
        self.tipoCesped = tipoCesped
        self.abierta = abierta

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Reserva:
    def __init__(self, cancha, cliente, horaReserva):
        self.cancha = cancha
        self.cliente = cliente
        self.horaReserva = horaReserva

class Club:
    def __init__(self):
        self.canchas = []
        self.reservas = []

    def agregarCancha(self):
        pass
    def eliminarCancha(self):
        pass
    def reservarCancha(self):
        pass
    def verReservas(self):
        pass
    def cancelarReserva(self):
        pass
    