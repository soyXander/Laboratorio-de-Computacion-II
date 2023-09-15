import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return math.pi * self.radio * 2
    
circ = Circulo(25)
print(circ.area())
print(circ.perimetro())