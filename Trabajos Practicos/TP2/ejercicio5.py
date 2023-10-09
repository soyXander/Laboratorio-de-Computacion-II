class Cancion:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion
        
    def __str__(self):
        return f"{self.titulo} - {self.autor} [{self.duracion} segs]"
    
class Album:
    def __init__(self, titulo):
        self.titulo = titulo
        self.canciones = []
        
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"La canción {cancion} se agrego correctamente al album")
    
    def numero_canciones(self):
        return f"El album contiene {len(self.canciones)} canciones"
    
    def eliminar_cancion(self, trackId):
        if trackId > 0:
            del self.canciones[trackId - 1]
        else:
            print("TrackID desconocido")
    
    def duracion_total(self):
        # duracion = 0
        # for c in self.canciones:
        #     duracion += c.duracion
        # return f"El album tiene una duracion de {duracion} segs"
        return f"El album tiene una duracion de {sum(c.duracion for c in self.canciones)} segs"
    
    def __str__(self):
        info = [f"=== Album {self.titulo} ==="]
        trackid = 1
        for c in self.canciones:
            info.append(str(trackid) + " - " + str(c))
            trackid += 1
        return '\n'.join(info)

cancion1 = Cancion("Cancion 1", "Autor 1", 123)
cancion2 = Cancion("Cancion 2", "Autor 2", 321)
cancion3 = Cancion("Cancion 3", "Autor 3", 321)

album = Album("Album piola")
album.agregar_cancion(cancion1)
album.agregar_cancion(cancion2)
album.agregar_cancion(cancion3)
print(album.duracion_total())
print(album)
album.eliminar_cancion(2)
print(album)