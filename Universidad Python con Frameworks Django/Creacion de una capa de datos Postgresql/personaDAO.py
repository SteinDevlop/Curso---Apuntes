
from conexion import Conexion
from persona import Persona
from manejo_de_loggin import *
import psycopg2
class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenercursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerconexion() as conexion:
            with Conexion.obtenercursor() as cursor:
                log.debug(f"Persona a insertar: {persona}")
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount
    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerconexion() as conexion:
            with Conexion.obtenercursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Persona actualizada:{persona}")
                return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerconexion() as conexion:
            with Conexion.obtenercursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Persona Eliminada:{persona}")
                return cursor.rowcount

if __name__ == '__main__':
    #Insertar registro
    #persona1 = Persona(nombre="Pedro", apellido="Najera",email="pnajera@gmail.com")
    #persona_insertada = PersonaDAO.insertar(persona1)
    #log.debug(f"Personas insertadas:{persona_insertada}")

    #actualizar
    #persona1=Persona(1,"ASA","RAZA","araza@gmail.com")
    #persona_actualizados= PersonaDAO.actualizar(persona1)
    #log.debug(f"Personas actualizados:{persona_actualizados}")

    #Eliminar
    persona1 = Persona(id_persona=3)
    persona_eliminada = PersonaDAO.eliminar(persona1)
    log.debug(f"Eliminaciones:{persona_eliminada}")

    #seleccion
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)