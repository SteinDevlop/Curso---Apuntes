import psycopg2 as db
import sys
from manejo_de_loggin import *

class Conexion:
    _DATABASE = "pyUni_db"
    _USERNAME = 'postgres'
    _PASSWORD = "admin"
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None
    @classmethod
    def obtenerconexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion =db.connect(
                user=cls._USERNAME,
                password=cls._PASSWORD,
                host=cls._HOST,
                port=cls._DB_PORT,
                database=cls._DATABASE)
                log.debug(f"Conexion exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                log.error(f"Ocurrio una excepcion: {e}")
                sys.exit()
        else:
            return cls._conexion


    @classmethod
    def obtenercursor(cls):
        if cls._cursor is None or cls._cursor.closed:
            try:
                cls._cursor=cls.obtenerconexion().cursor()
                log.debug(f"Se abrio correctamente el cursor: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error(f"Ocurrio uan excepcion al obtener cursor: {e}")
                sys.exit()
        else:
            return cls._cursor

if __name__ == "__main__":
    Conexion.obtenerconexion()
    Conexion.obtenercursor()