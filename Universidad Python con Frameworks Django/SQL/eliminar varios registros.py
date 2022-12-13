from conexion import *
import psycopg2
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM persona WHERE id_persona IN %s"
            entrada = (input("IDs a eliminar (separelos por coma): "))
            valores = (tuple(entrada.split(",")),)
            #El metodo split regresa una lista [x,x,x,x], lo forzamos a ser una tupla
            cursor.execute(sentencia,valores) #aca se mantiene solo execute
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")
except Exception as e:
    print(e)
finally:
    conexion.close()