class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def perimetro(self):
        return f"Perimetro: {self.ladoA + self.ladoB + self.ladoC}"
    
    def esEquilatero(self):
        return self.ladoA == self.ladoB and self.ladoB == self.ladoC

    def esIsoscele(self):
        return self.ladoA == self.ladoB != self.ladoC or self.ladoA == self.ladoC != self.ladoB or self.ladoB == self.ladoC != self.ladoA

    def esEscaleno(self):
        return self.ladoA != self.ladoB != self.ladoC
    
tri = Triangulo(1, 1, 1)
print(tri.perimetro())
print(tri.esEquilatero())
print(tri.esIsoscele())
print(tri.esEscaleno())