import psycopg2 as db
from psycopg2 import pool
import sys
from manejo_de_loggin import *

class Conexion:
    _DATABASE = "pyUni_db"
    _USERNAME = 'postgres'
    _PASSWORD = "admin"
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONEXION = 1
    _MAX_CONEXION = 5
    _POOL = None

    @classmethod
    def obtener_pool(cls):
        if cls._POOL is None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MIN_CONEXION,cls._MAX_CONEXION,host = cls._HOST,user = cls._USERNAME,password = cls._PASSWORD,port = cls._DB_PORT,database = cls._DATABASE)  # la forma mas facil de obtener un pool
                log.debug(f"Creacion del pool exitosa:{cls._POOL}")
                return cls._POOL
            except Exception as e:
                log.error(f"Ha ocurrido un error al inicializar el pool. Error:{e}")
                sys.exit()
        else:
            return cls._POOL
    @classmethod
    def obtenerconexion(cls):
        conexion = cls.obtener_pool().getconn() 
        #llamamos a la conexion del pool
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion
if __name__ == "__main__":
    conexion1=Conexion.obtenerconexion()
    print("----------")
    conexion2=Conexion.obtenerconexion()
    print("----------")
    conexion3=Conexion.obtenerconexion()
    print("----------")
    conexion4=Conexion.obtenerconexion()
    print("----------")
    conexion5=Conexion.obtenerconexion()