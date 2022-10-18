from FiguraGeometrica import *
from Color import *
from Rectangulo import *
from Cuadrado import *
print("Rectangulo".center(50,"-"))
test1 = Rectangulo(0,5,"Verde")
print(f"Area del rectangulo: {test1.calcular_area()}")
print(test1)

print("Cuadrado".center(50,"-"))
test2 = Cuadrado(7,"Verde")
print(f"Area del rectangulo: {test2.calcular_area()}")
print(test2)