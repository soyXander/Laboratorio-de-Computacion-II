class Persona:
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        
    def nombreCompleto(self):
        return f"{self.apellido}, {self.nombre}"
    
    def esMayor(self):
        return self.edad >= 18
    
    def imc(self):
        return f"IMC: {self.peso / (self.altura ** 2)}"
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.edad} años, {self.altura} mts, {self.peso} kgs."
    
p = Persona("Mengano", "Fulano", 30, 1.65, 100)
print(p.nombreCompleto())
print(p.esMayor())
print(p.imc())
print(p)