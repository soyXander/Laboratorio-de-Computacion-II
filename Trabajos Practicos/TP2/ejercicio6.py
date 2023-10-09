class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return f"{self.titulo} - {self.autor} [{self.paginas} paginas]"
    
class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def ordenar_lista_por_titulo(self):
        self.libros.sort(key=lambda libro: libro.titulo)
        
    def numero_libros(self):
        return f"Cantidad de libros en la biblioteca: {len(self.libros)}"
    
    def eliminar_libro(self, index):
        if index >= 0 and index < len(self.libros):
            del self.libros[index]
        else:
            print("Indice fuera de rango")
        
    def __str__(self):
        info = [f"=== Libros en la Biblioteca ==="]
        for l in self.libros:
            info.append(str(l))
        return '\n'.join(info)
    
libro1 = Libro("Fdas", "Autor 1", 56)
libro2 = Libro("Badas 2", "Autor 2", 77)
libro3 = Libro("Asds 3", "Autor 3", 145)

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
print(biblioteca.numero_libros())
print(biblioteca)
biblioteca.ordenar_lista_por_titulo()
print(biblioteca)
biblioteca.eliminar_libro(1)
print(biblioteca)