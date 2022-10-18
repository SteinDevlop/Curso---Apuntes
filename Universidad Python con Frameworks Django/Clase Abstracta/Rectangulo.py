from FiguraGeometrica import *
from Color import *


class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,alto, ancho, color):
        #super().__init__(ancho, alto) #aca hay cierto problema, se manda a llamar siempre la primera clase que aparece como la padre en la clase.
        FiguraGeometrica.__init__(self,alto,ancho) #usamos una forma alterna, llamamos la funcion init de la clase FiguraGeometrica
        self._ancho = ancho
        self._alto = alto
        Color.__init__(self,color)    
        self._color = color

    #Encapsulamiento

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self,alto):
        self._alto = alto

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho

    #Fin de encapsulamiento
    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}"
    def calcular_area(self):
        return self.alto * self.ancho

