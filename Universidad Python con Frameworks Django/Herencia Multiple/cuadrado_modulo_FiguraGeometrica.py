#importamos las clases (lo renombraos con As)
from FiguraGeometrica import FiguraGeometrica
from color_modulo_figuraGeometrica import Color


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado, color):
        #super().__init__(ancho, alto) #aca hay cierto problema, se manda a llamar siempre la primera clase que aparece como la padre en la clase.
        FiguraGeometrica.__init__(self,lado,lado) #usamos una forma alterna, llamamos la funcion init de la clase FiguraGeometrica
        
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
    
    def calcular_area(self):
        return self.alto * self.ancho