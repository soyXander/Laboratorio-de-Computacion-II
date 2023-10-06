class CuentaBancaria:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = 0
        
    def __str__(self):
        return f"{self.apellido}, {self.nombre} - Saldo ${self.saldo}."
    
    def saldo(self):
        return f"Saldo de la cuenta: ${self.saldo}."
    
    def ingresar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se ingreso ${monto} a la cuenta.")
        else:
            print("El saldo a ingresar debe ser positivo.")
            
    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Se retiro ${monto} de la cuenta.")
            else:
                print("El monto a retirar supera el saldo de la cuenta.")
        else:
            print("El monto a retirar debe ser positivo.")
            
class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.activa = False

    def __str__(self):
        # if self.activa:
        #     activa = "Activa"
        # else:
        #     activa = "Inactiva"
        activa = "Activa" if self.activa else "Inactiva"
        return f"{super().__str__()} (Cuenta {activa})"
        
    def ingresar(self, monto):
        super().ingresar(monto)
        if self.saldo < 10000:
            self.activa = False
        else:
            self.activa = True

    def retirar(self, monto):
        if self.activa:
            super().retirar(monto)
            if self.saldo < 10000:
                self.activa = False
        else:
            print("La cuenta se encuentra inactiva, no se puede realizar retiros.")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.sobregiro = 0
    
    def __str__(self):
        return f"{super().__str__()} - Sobregiro: ${self.sobregiro}"

    def ingresar(self, monto):
        if monto > 0:
            if self.sobregiro > 0:
                if monto <= self.sobregiro:
                    print(f"Se ingreso ${monto} a la cuenta. Se desconto del sobregiro de ${self.sobregiro}.")
                    self.sobregiro -= monto
                else:
                    self.saldo += (monto - self.sobregiro)
                    self.sobregiro = 0
                    print(f"Se ingreso ${monto} a la cuenta. Se desconto del sobregiro de ${self.sobregiro}.")
            else:
                super().ingresar(monto)
        else:
            print("El monto debe ser positivo.")
            
    def retirar(self, monto):
        if monto > 0:
            if self.saldo >= monto:
                super().retirar(monto)
            else:
                self.sobregiro += monto - self.saldo
                self.saldo = 0
                print(f"Se retiro ${monto} de la cuenta. Se genero un sobregiro de ${self.sobregiro}.")
        else:
            print("El monto debe ser positivo.")

print("=== Cuenta Ahorro ===")
cntAhorro = CuentaAhorro("Fabian", "Brizuela")
print(cntAhorro)
cntAhorro.ingresar(10000)
print(cntAhorro)
cntAhorro.retirar(11000)
cntAhorro.retirar(4000)
print(cntAhorro)
cntAhorro.ingresar(2000)
print(cntAhorro)

print()
print("=== Cuenta Corriente ===")
cntCorriente = CuentaCorriente("Carlos", "Carrizo")
print(cntCorriente)
cntCorriente.ingresar(10000)
print(cntCorriente)
cntCorriente.retirar(15000)
print(cntCorriente)
cntCorriente.ingresar(2000)
print(cntCorriente)