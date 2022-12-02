class Pelicula:
    def __init__(self,nombre) -> None:
        self._nombre = nombre
    #encapsulamiento de nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    #cierre de encapsulamiento
    def __str__(self):
        return f"Pelicula: {self._nombre}"