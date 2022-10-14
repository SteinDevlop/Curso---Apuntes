class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @property #es un decorador, para acceder al metodo anterior como si fuera un atributo, entonces solo lo accedemos como si fuese un atributo
    def nombre(self):
        return self._nombre #con esto recuperamos el valor de nombre sin acceder a el directamente

persona1 = Persona("Juan", "Perez", 28)
print(persona1.mostrar_detalle())
