class CuentaBancaria:
    def __init__(self, nombre, apellido, nCuenta, saldo = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.nCuenta = nCuenta
        self.saldoActual = saldo
        self.historial = []
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre} - ${self.saldoActual} ({self.nCuenta})"
    
    def saldo(self):
        return f"Saldo de la cuenta {self.nCuenta}: ${self.saldoActual}"
        
    def ingresar(self, monto):
        if monto > 0:
            self.saldoActual += monto
            self.historial.append(f"- Ingreso: +${monto} || Saldo: ${self.saldoActual}")
            return f"Se ingreso el monto de ${monto} a la cuenta {self.nCuenta}. Saldo actual: ${self.saldoActual}"
        else:
            return "No se puede ingresar el monto ingresado. Debe ser un monto positivo"
            
    def retirar(self, monto):
        if monto > 0 and monto <= self.saldoActual:
            self.saldoActual -= monto
            self.historial.append(f"- Retiro: -${monto} || Saldo: ${self.saldoActual}")
            return f"Se retiro ${monto} del saldo de la cuenta Nº {self.nCuenta}. Saldo actual: ${self.saldoActual}"
        else:
            return "No se puede retirar el monto ingresado. El monto debe ser positivo y menor o igual al saldo de la cuenta"

    def verHistorial(self):
        print(f"Movimientos de la cuenta: {self.nCuenta}")
        for e in self.historial:
            print(e)
        
fulano = CuentaBancaria("Cosme", "Fulanito", 12365478)
print(fulano)
print(fulano.saldo())
print(fulano.ingresar(1200))
print(fulano.retirar(250))
print(fulano.verHistorial())