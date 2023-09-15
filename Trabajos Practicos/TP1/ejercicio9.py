class Cola:
    def __init__(self):
        self.cola = []
        
    def agregar(self, elem):
        self.cola.append(elem)
        
    def quitar(self):
        return f"Elemento eliminado: {self.cola.pop()}"
        
    def estaVacia(self):
        return len(self.cola) == 0
        
    def cantidad(self):
        return len(self.cola)
        
c = Cola()
print(c.estaVacia())
c.agregar(1)
c.agregar(2)
c.agregar(3)
print(c.cola)
print(c.quitar())
print(c.cola)
print(c.estaVacia())