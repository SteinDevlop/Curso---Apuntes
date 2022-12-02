import os
class Catalogo_De_Peliculas:
    ruta = "pelicula.txt"
    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta,"a",encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")
            print("Pelicula Agregada")
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta,"r",encoding="utf8") as archivo:
            for lineas in archivo:
                print(lineas)
    @classmethod
    def eliminar_archivo(cls):
        os.remove(cls.ruta)
        print(f"Archivo eliminado: {cls.ruta}")