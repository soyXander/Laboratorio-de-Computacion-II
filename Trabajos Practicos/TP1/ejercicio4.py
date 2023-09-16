class Cafetera:
    def __init__(self, capacidadMaxima = 1000, cantidadActual = 0):
        self.capacidadMaxima = capacidadMaxima
        self.cantidadActual = cantidadActual

    def llenar(self):
        self.cantidadActual = self.capacidadMaxima
        return "Se lleno la cafetera"

    def servir(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidadActual:
            self.cantidadActual -= cantidad
            return f"Se sirvio {cantidad}cc. de café"
        else:
            return "No se puede servir la cantidad deseada"

    def vaciar(self):
        self.cantidadActual = 0
        return "Se vacio la cafetera"

    def agregar(self, cantidad):
        if cantidad > 0:
            if self.cantidadActual + cantidad <= self.capacidadMaxima:
                self.cantidadActual += cantidad
                return f"Se agrego {cantidad}cc. de cafe a la cafetera"
            else:
                return "La cantidad a agregar superar a la capacidad maxima"
        else:
            return "No se puede agregar una cantidad negativa"

caf = Cafetera()
print(caf.llenar())
print(caf.servir(100))
print(caf.vaciar())
print(caf.agregar(300))
