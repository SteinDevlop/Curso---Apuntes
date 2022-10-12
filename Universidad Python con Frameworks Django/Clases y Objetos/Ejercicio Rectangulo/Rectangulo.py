class Rectangulo:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base
    def area_clase(self):
        return self.altura * self.base

altura=float(input("Indique la altura del rectangulo: "))
base=float(input("Indique la base del rectangulo: "))
area=Rectangulo(altura,base)
print(f"El area del rectangulo es: {area.area_clase()}")