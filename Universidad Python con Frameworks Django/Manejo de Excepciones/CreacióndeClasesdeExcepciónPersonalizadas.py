#Ejemplo de numeros identicos
class NumerosIdenticosException(Exception):
    def __init__(self,mensaje) -> None:
        self.messaje = mensaje