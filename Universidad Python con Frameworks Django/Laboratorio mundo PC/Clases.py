class Orden:
    pass
class Computadora:
    pass
class Monitor:
    pass
class DispositivoEntrada:
    def __init__(self,tipoEntrada,marca) -> None:
        self.__tipoEntrada = tipoEntrada
        self.__marca = marca
class Raton(DispositivoEntrada):
    pass
class Teclado(DispositivoEntrada):
    pass
