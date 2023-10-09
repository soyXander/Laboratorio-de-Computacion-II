class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        
class Moto(Vehiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.valor_peaje = 150

class Auto(Vehiculo):
    def __init__(self, placa):
        super().__init__(placa)
        self.valor_peaje = 300

class Camion(Vehiculo):
    def __init__(self, placa, cantidad_ejes):
        super().__init__(placa)
        self.cantidad_ejes = cantidad_ejes
        self.valor_peaje = 500 * cantidad_ejes

class Peaje:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        self.vehiculos = []
        self.total_peaje = 0

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        self.total_peaje += vehiculo.valor_peaje

    def calcular_total_peaje(self):
        print(f"Total de peajes recolectados en {peaje1.nombre}, {peaje1.departamento}: ${self.total_peaje}")

    def cantidad_vehiculos(self):
        print(f"Cantidad de vehiculos en {peaje1.nombre}: {len(self.vehiculos)}")

peaje1 = Peaje("Peaje 1", "Dpto 1")

moto1 = Moto("A123BCD")
auto1 = Auto("AA321BC")
camion1 = Camion("AC456DE", 4)

peaje1.agregar_vehiculo(moto1)
peaje1.agregar_vehiculo(auto1)
peaje1.agregar_vehiculo(camion1)

peaje1.calcular_total_peaje()
peaje1.cantidad_vehiculos()
