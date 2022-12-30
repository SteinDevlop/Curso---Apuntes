from logger_base import log
from psycopg2 import pool
import sys

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
    def obtenerPool(cls):
        if cls._POOL is None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MIN_CONEXION, cls._MAX_CONEXION,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._POOL}')
                return cls._POOL
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._POOL

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
