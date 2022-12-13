from conexion import *
import psycopg2
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM persona WHERE id_persona=%s"
            entrada = int(input("ID a eliminar: "))
            valores = (entrada,)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")
except Exception as e:
    print(e)
finally:
    conexion.close()