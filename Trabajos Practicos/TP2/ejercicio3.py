import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Linea:
    def __init__(self, a, b):
        self.punto_a = a
        self.punto_b = b
        
    def __str__(self):
        return f"(({self.punto_a.x},{self.punto_a.y}), ({self.punto_b.x},{self.punto_b.y}))"

    def distancia(self):
        return math.sqrt((self.punto_a.x - self.punto_b.x) ** 2 + (self.punto_a.y - self.punto_b.y) ** 2)

    def mover_derecha(self, cantidad):
        self.punto_a.x += cantidad
        self.punto_b.x += cantidad

    def mover_izquierda(self, cantidad):
        self.punto_a.x -= cantidad
        self.punto_b.x -= cantidad

    def mover_arriba(self, cantidad):
        self.punto_a.y += cantidad
        self.punto_b.y += cantidad

    def mover_abajo(self, cantidad):
        self.punto_a.y -= cantidad
        self.punto_b.y -= cantidad
    
p1 = Punto(1, 2)
p2 = Punto(5, 3)
linea = Linea(p1, p2)

print(f"Posición: {linea}")
print(f"Distancia entre puntos: {linea.distancia()}")

linea.mover_derecha(3)
print(f"Posición: {linea}")

linea.mover_abajo(2)
print(f"Posición: {linea}")