class Inmueble:
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta):
        self.identificador = identificador
        self.cantidad_habitaciones = cantidad_habitaciones
        self.area = area
        self.direccion = direccion
        self.precio_venta = precio_venta
    
    def calcular_precio(self, valor_area):
        precio_venta = self.area * valor_area
        return precio_venta
    
    def __str__(self):
        return f'''Identificador: {self.identificador}
Habitaciones: {self.cantidad_habitaciones}
Area: {self.area} mts²
Dirección: {self.direccion}
Precio de venta: ${self.precio_venta}'''

class Casa(Inmueble):
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos):
        super().__init__(identificador, cantidad_habitaciones, area, direccion, precio_venta)
        self.cantidad_pisos = cantidad_pisos
    
    def __str__(self):
        return f'''{super().__str__()}
Cantidad de pisos: {self.cantidad_pisos}'''

class Departamento(Inmueble):
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta, numero_piso):
        super().__init__(identificador, cantidad_habitaciones, area, direccion, precio_venta)
        self.numero_piso = numero_piso
    
    def __str__(self):
        return f'''{super().__str__()}
Numero de piso: {self.numero_piso}'''

class CasaRural(Casa):
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos, distancia, altitud):
        super().__init__(identificador, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos)
        self.distancia = distancia
        self.altitud = altitud
        
    def __str__(self):
        return f'''{super().__str__()}
Distancia: {self.distancia}
Altitud: {self.altitud}'''

class CasaUrbana(Casa):
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos, tiene_pileta):
        super().__init__(identificador, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos)
        self.tiene_pileta = tiene_pileta
    
    def __str__(self):
        return f'''{super().__str__()}
Tiene pileta: {"Si" if self.tiene_pileta else "No"}'''

class DepartamentoFamiliar(Departamento):
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta, numero_piso, cantidad_familiares):
        super().__init__(identificador, cantidad_habitaciones, area, direccion, precio_venta, numero_piso)
        self.cantidad_familiares = cantidad_familiares
    
    def __str__(self):
        return f'''{super().__str__()}
Cantidad de familiares: {self.cantidad_familiares}'''

class DepartamentoEstudio(Departamento):
    def __init__(self, identificador, cantidad_habitaciones, area, direccion, precio_venta, numero_piso, cantidad_empleados):
         super().__init__(identificador, cantidad_habitaciones, area, direccion, precio_venta, numero_piso)
         self.cantidad_empleados = cantidad_empleados
         
    def __str__(self):
        return f'''{super().__str__()}
Cantidad de empleados: {self.cantidad_empleados}'''
    
casar = CasaRural(1, 5, 1500, "RN 75", 25000000, 1, 2.5, 1200)
print("== Casa Rural ==")
print(casar)
print()
print("== Casa Urbana ==")
casau = CasaUrbana(2, 5, 300, "Av Siempre Viva, 321", 3500000, 2, True)
print(casau)
print()

print("== Depto Familiar ==")
deptof = DepartamentoFamiliar(3, 4, 150, "Av Porahi, 101", 2200000, 15, 4)
print(deptof)
print()
print("== Depto Estudio ==")
deptoe = DepartamentoEstudio(4, 2, 80, "Av Porahi, 202", 2500000, 2, 10)
print(deptoe)
