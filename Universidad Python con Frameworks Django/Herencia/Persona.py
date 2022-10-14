#Herencia simple
class Persona(object): #de manera implicita si no se deice lo contrario todas las clases vienen de la clase object
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self) -> str:
        return f"Persona: {self.nombre}, {self.edad}"
    
class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo):
        super().__init__(nombre, edad) #traer la informacion de la clase padre
        self.sueldo = sueldo
    def __str__(self) -> str:
        return f"{super().__str__()},{self.sueldo}"

