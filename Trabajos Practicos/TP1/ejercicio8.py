class Pila:
    def __init__(self):
        self.pila = []
        
    def agregar(self, elem):
        self.pila.append(elem)
        
    def quitar(self):
        return f"Elemento eliminado: {self.pila.pop(0)}"
        
    def estaVacia(self):
        return len(self.pila) == 0
        
    def cantidad(self):
        return len(self.pila)
        
p = Pila()
print(p.estaVacia())
p.agregar(1)
p.agregar(2)
p.agregar(3)
print(p.pila)
print(p.quitar())
print(p.pila)
print(p.estaVacia())