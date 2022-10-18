from FiguraGeometrica import *
from Color import *


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado, color):
        FiguraGeometrica.__init__(self,lado,lado)
        
        Color.__init__(self,color)    
        self._lado = lado
        self._color = color

    #Encapsulamiento

    @property
    def lado(self):
        return self._lado
    @lado.setter
    def lado(self,lado):
        self._lado = lado

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color

    #Fin de encapsulamiento
    def __str__(self) -> str:
        return f"{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}"
    def calcular_area(self):
        return self.alto * self.ancho

