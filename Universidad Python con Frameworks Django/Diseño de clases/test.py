from producto import Producto
from orden import Orden
if __name__== "__main__":
    producto1 = Producto("Camisa",100.00)
    producto2 = Producto("Pantalon",105.00)
    producto3 = Producto("Collar",43.00)
    producto4 = Producto("Zapatos",600.00)
    productos1 = [producto1,producto2]
    productos2 = [producto3,producto4]
    orden1 = Orden(productos1)
    orden2 = Orden(productos2)
    print(orden1)
    print(f"Total de orden 1: {orden1.calcular_total_deLa_orden()}")
    print(orden2)
    print(f"Total de orden 2: {orden2.calcular_total_deLa_orden()}")
    #agregamos producto
    producto5 = Producto("Pacha",140.00)
    orden1.agregar_producto(producto5)
    print(orden1)