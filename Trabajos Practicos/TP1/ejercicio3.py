class Contador:
    def __init__(self, cuenta = 0):
        self.cuenta = cuenta
    
    def mostrar(self):
        print('Estado de la cuenta:', self.cuenta)
        
    def incrementar(self, valor = 1):
        self.cuenta += valor
    
    def decrementar(self, valor = 1):
        self.cuenta -= valor
    
    def reiniciar(self):
        self.cuenta = 0
        
cont = Contador(10)

cont.mostrar()
cont.incrementar(2)
cont.mostrar()
cont.decrementar(4)
cont.mostrar()
