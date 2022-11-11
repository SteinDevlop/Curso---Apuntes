from ClaseEmpleado import Empleado
from ClaseGerente import Gerente

def imprimir_detalles(obj):
    print(obj)
    print(type(obj))

empleado = Empleado("Carlos",50000)
imprimir_detalles(empleado)
print("\n")
gerente = Gerente("Maria",80000,"Sistemas")
imprimir_detalles(gerente)

#notemos que usando una funcion llamamos multiples clases