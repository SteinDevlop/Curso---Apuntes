import psycopg2 as db
class Conexion:
    conexion = None
    def obtenerconexion(cls):
        try:
            conexion = db.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='pyUni_db')
        except Exception as e:
            print(f"Error al conectar base de datos, Detalle: {type(e)}")

    def obtenercursor(cls):
        try:
            with conexion:
                cursor = conexion.cursor()
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def cerrar(cls):
        pass
