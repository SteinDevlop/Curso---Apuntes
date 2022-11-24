class Computadora:
    contador_computadora = 0
    def __init__(self,nombre,monitor,teclado,raton) -> None:
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    def __str__(self) -> str:
        return f"""
        Nombre: {self._nombre}   Id: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        """