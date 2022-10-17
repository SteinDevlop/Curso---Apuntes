class FiguraGeometrica:
    def __init__(self,ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    #Encapsulamiento

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def nombre(self,ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    @ancho.setter
    def alto(self,alto):
        self._alto = alto

    #Fin del encapsulamiento
