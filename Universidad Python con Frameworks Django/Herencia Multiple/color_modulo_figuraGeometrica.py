class Color:
    def __init__(self,color):
        self._color = color
    
    #Encapsulamiento

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color

    #Fin de encapsulamiento