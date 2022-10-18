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
    #me falto poner el __str__

    #agregado:
    def __str__(self):
        return f"Color: {self.color}"
    #Fin de encapsulamiento