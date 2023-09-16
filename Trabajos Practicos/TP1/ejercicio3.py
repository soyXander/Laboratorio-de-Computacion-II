class Contador:
    def __init__(self, cuenta = 0):
        self.cuenta = cuenta
    
    def mostrar(self):
        print(f"Contador: {self.cuenta}")
        
    def incrementar(self, valor = 1):
        self.cuenta += valor
        print(f"Se incremento {valor} a la cuenta.")
    
    def decrementar(self, valor = 1):
        self.cuenta -= valor
        print(f"Se decremento {valor} a la cuenta.")
    
    def reiniciar(self):
        self.cuenta = 0
        print(f"Se reinicio la cuenta a 0.")
        
cont = Contador(10)
cont.mostrar()
cont.incrementar(2)
cont.mostrar()
cont.decrementar(4)
cont.mostrar()
