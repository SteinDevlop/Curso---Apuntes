class Orden:
    contador_ordenes = 0
    @classmethod
    def _generarcontador_ordenes(cls):
        Orden.contador_ordenes += 1
        return Orden.contador_ordenes
    def agregar_computadora(self,computadora):
        self.computadoras.append(computadora)
    def __init__(self,computadoras):
        self.id_orden = Orden.generarcontador_ordenes()
        self.computadoras = list(computadoras)
    
    def __str__(self) -> str:
        computadoras_str = ""
        for Computadora in self.computadoras:
            computadoras_str += Computadora.__str__() + '\n'
        return f"Orden → Id: {self.id_orden} | Computadoras: \n{computadoras_str}"
class Computadora:
    pass
class Monitor:
    pass
