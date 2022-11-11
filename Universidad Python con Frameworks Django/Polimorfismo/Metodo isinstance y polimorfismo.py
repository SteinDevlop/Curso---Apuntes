from ClaseEmpleado import Empleado
from ClaseGerente import Gerente

def imprimir_detalles(obj):
    print(obj)
    print(type(obj))
    #si la instancia de un objeto contiene un valor especifico, que no esta en otras usamos:
    if isinstance(obj,Gerente):
        print(obj.departamento)

empleado = Empleado("Carlos",50000)
gerente = Gerente("Maria",80000,"Sistemas")

imprimir_detalles(gerente)
