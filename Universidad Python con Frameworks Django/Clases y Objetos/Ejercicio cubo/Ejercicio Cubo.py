class Cubo:
    def __init__(self, alto, profundidad, ancho) -> float:
        self.alto=alto
        self.profundidad=profundidad
        self.ancho=ancho
    def calcular_volumen(self):
        return (self.alto*self.ancho*self.profundidad)

alto = float(input("Indique el alto del cubo: "))
ancho = float(input("Indique el ancho del cubo: "))
profundo = float(input("Indique lo profundo que es el cubo: "))

volumen = Cubo(alto,ancho,profundo)
print(f"El volumen del cubo es: {(volumen.calcular_volumen()):.2f}")