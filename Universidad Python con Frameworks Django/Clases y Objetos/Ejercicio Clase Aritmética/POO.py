class Aritmetica:
    """
    Clase aritmetica, para realizar x operaciones
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB
    def elevar(self):
        return self.operandoA ** self.operandoB

aritmetica1=Aritmetica(2,5)
print(aritmetica1.sumar())