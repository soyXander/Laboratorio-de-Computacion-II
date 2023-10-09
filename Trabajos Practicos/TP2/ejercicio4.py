class Motor:
    def __init__(self, nivel_aceite = 100, temperatura = 0, encendido = False):
        self.nivel_aceite = nivel_aceite
        self.temperatura = temperatura
        self.encendido = encendido

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print("Se arranco el motor")
        else:
            print("El motor ya esta en marcha")

    def detener(self):
        if self.encendido:
            self.encendido = False
            print("Se detuvo el motor")
        else:
            print("El motor ya esta detenido")

class Rueda:
    def __init__(self, rodado, presion=40):
        self.rodado = rodado
        self.presion = presion

    def inflar(self, presion = 1):
        self.presion += presion
        print(f"Se inflo la rueda. Presión actual: {self.presion}")

    def desinflar(self, presion = 1):
        self.presion -= presion
        print(f"Se desinflo la rueda. Presión actual: {self.presion}")

class Ventana:
    def __init__(self, polarizado = False):
        self.polarizado = polarizado
        self.abierta = False

    def abrir(self):
        if not self.abierta:
            self.abierta = True
            print("Se abrio la ventana")
        else:
            print("La ventana ya esta abierta")

    def cerrar(self):
        if self.abierta:
            self.abierta = False
            print("Se cerro la ventana")
        else:
            print("La ventana ya esta cerrada")

class Puerta:
    def __init__(self, color, ventana):
        self.color = color
        self.ventana = ventana
        self.abierta = False

    def abrir(self):
        if not self.abierta:
            self.abierta = True
            print("Se abrio la puerta")
        else:
            print("La puerta ya esta abierta")

    def cerrar(self):
        if self.abierta:
            self.abierta = False
            print("Se cerro la puerta")
        else:
            print("La puerta ya esta cerrada")

class Auto:
    def __init__(self, motor, ruedas, puertas):
        self.motor = motor
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        motor = f"Motor: Nivel de aceite: {self.motor.nivel_aceite}%, Temperatura: {self.motor.temperatura}, Encendido: {'Si' if self.motor.encendido else 'No'}"
        ruedas = "\n".join([f"Rueda {rueda.rodado} - Presión: {rueda.presion}" for rueda in self.ruedas])
        puertas = "\n".join([f"Puerta {puerta.color} - Polarizada: {'Si' if puerta.ventana.polarizado else 'No'}" for puerta in self.puertas])

        return f"=== Info del Auto ===\n{motor}\n\nRuedas:\n{ruedas}\n\nPuertas:\n{puertas}\n"

motor = Motor()
ruedas = [Rueda("14"), Rueda("14"), Rueda("14"), Rueda("14")]
puertas = [Puerta("Verde", Ventana(True)), Puerta("Azul", Ventana(False))]

auto = Auto(motor, ruedas, puertas)

print(auto)