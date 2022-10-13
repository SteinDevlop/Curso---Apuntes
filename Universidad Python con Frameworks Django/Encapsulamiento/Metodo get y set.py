class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @property #es un decorador, para acceder al metodo anterior como si fuera un atributo, entonces solo lo accedemos como si fuese un atributo
    def nombre(self):
        return self._nombre #con esto recuperamos el valor de nombre sin acceder a el directamente
    @nombre.setter #setter es para cambiar el valor de los datos, tambien es un decorador
    def nombre(self,nombre):
        self._nombre = nombre
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1 = Persona("Juan", "Perez", 28)
print(persona1.mostrar_detalle())
persona1.nombre="Carlitos"
print(persona1.mostrar_detalle())
