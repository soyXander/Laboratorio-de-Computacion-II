class Cafetera:
    def __init__(self, capacidadMaxima = 1000, cantidadActual = 0):
        self.capacidadMaxima = capacidadMaxima
        self.cantidadActual = cantidadActual

    def llenar(self):
        self.cantidadActual = self.capacidadMaxima
        print("Se lleno la cafetera")

    def servir(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidadActual:
            self.cantidadActual -= cantidad
            print(f"Se sirvio {cantidad}cc. de café")
        else:
            print("No se puede servir la cantidad deseada")

    def vaciar(self):
        self.cantidadActual = 0
        print("Se vacio la cafetera")

    def agregar(self, cantidad):
        if cantidad > 0:
            if self.cantidadActual + cantidad <= self.capacidadMaxima:
                self.cantidadActual += cantidad
                print(f"Se agrego {cantidad}cc. de cafe a la cafetera")
            else:
                print("La cantidad a agregar superar a la capacidad maxima")
        else:
            print("No se puede agregar una cantidad negativa")

caf = Cafetera()
caf.llenar()
caf.servir(100)
caf.vaciar()
caf.agregar(300)
