class FiguraGeometrica:
    def __init__(self,ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo alto: {alto}')
    
    #Encapsulamiento

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def nombre(self,ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto
    @ancho.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    #Fin del encapsulamiento

    def __str__(self) -> str:
        return f"Ancho: {self.ancho}, Alto: {str(self.alto)}"
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False