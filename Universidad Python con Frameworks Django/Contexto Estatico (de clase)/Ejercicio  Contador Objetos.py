from ast import Pass


class Persona:
    contadorPorPersona = 0
    @classmethod
    def _generarContadorPersona(cls):
        Persona.contadorPorPersona += 1
        return Persona.contadorPorPersona
    def __init__(self,nombre,edad):
        self.id_persona = Persona.generarContadorPersona()
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"[Nombre: {self.nombre}, Edad: {self.edad}, ID: {self.id_persona}]"
        print
persona1=Persona("Alejandro",17)
persona2=Persona("Mariana",15)
print(persona1)
print(persona2)
