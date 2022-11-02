class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __add__(self,other):
        #self: primer operando
        #other, segundo operando
        return f"{self.nombre} {other.nombre}"
    def __sub__(self,other):
        return f"{self.edad - other.edad}"
persona1 = Persona("Juan",34)
persona2 = Persona("Maria",12) 
print(persona1+persona2)
print(persona1-persona2)