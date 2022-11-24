class DispositivoEntrada:
    def __init__(self,tipoEntrada,marca) -> None:
        self._tipoEntrada = tipoEntrada
        self._marca = marca
class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, tipoEntrada, marca) -> None:
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(tipoEntrada, marca)
    def __str__(self) -> str:
        return f"Id: {self._id_raton}, Marca: {self._marca}, Tipo Entrada: {self._tipoEntrada}"
class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, tipoEntrada, marca) -> None:
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(tipoEntrada, marca)
    def __str__(self) -> str:
        return f"Id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipoEntrada}"
        