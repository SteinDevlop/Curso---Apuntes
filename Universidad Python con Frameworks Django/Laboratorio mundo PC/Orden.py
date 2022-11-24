class Orden:
    contador_ordenes = 0
    def __init__(self,computadoras) -> None:
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)
    def agregarComputadora(self,computadora):
        self._computadoras.append(computadora)
    def __str__(self) -> str:
        computadora_str = ""
        for computadora in self._computadoras:
            computadora_str += computadora.__str__()
        return f"""
        Orden: {self._id_orden}
        Computadoras: {computadora_str}
        
        """
