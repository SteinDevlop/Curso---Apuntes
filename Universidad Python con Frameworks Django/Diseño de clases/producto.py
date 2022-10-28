class Producto:
    contador_producto = 0

    def __init__(self,nombre,precio):
        Producto.contador_producto += 1
        self._id_producto = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def id_producto(self,id_producto):
        self._id_producto = Producto.contador_producto

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio
        
    def __str__(self) -> str:
        return f"ID Producto: {int(self.id_producto)}, Nombre: {self.nombre}, Precio: {float(self.precio):.2f}"

if __name__ == "__main__":
    producto1 = Producto("Repelente",50000)
    producto2 = Producto("Mentas",200)
    print(producto1)
    print(producto2)
else:
    pass