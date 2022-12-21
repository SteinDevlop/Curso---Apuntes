from manejo_de_loggin import *
class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._id_persona = id_persona
    
    def __str__(self) -> str:
        return f"""
        ID: {self._id_persona}
        Nombre:{self._nombre} , Apellido:{self._apellido}
        Email:{self._email}"""
    
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self,id_persona):
        self._id_persona=id_persona

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
        
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email=email
if __name__ == "__main__":
    persona1=Persona(nombre="Juan",apellido="Sarza",email="jSarza@gmail.com")
    log.debug(persona1)