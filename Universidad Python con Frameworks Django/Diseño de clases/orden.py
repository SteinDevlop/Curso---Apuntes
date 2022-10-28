from producto import Producto
class Orden:
    contador_orden = 0

    def __init__(self,productos):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        self.productos = list(productos)

    def agregar_producto(self,producto):
        self.productos.append(producto)
    def calcular_total_deLa_orden(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total
    def __str__(self) -> str:
        productos_str = ""
        for producto in self.productos:
            productos_str += producto.__str__()+"\n"
        return f"Orden: {self.id_orden},\nProductos: {productos_str}"

if __name__ == "__main__":
    producto1 = Producto("Camisa",100.00)
    producto2 = Producto("Pantalon",105.00)
    producto3 = Producto("Collar",43.00)
    productos1 = [producto1,producto2,producto3]
    orden1 = Orden(productos1)
    print(orden1)