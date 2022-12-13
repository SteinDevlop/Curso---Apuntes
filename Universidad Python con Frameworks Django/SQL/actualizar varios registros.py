from conexion import *
import psycopg2
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s,email=%s WHERE id_persona=%s"
            valores = (
                ("Pedro","Calvo","Pcalvo@gmail.com",2), #Bien bld se me paso una coma
                ("Rata","Tasta","Rtasta@gmail.com",3)
            )
            cursor.executemany(sentencia,valores)
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(e)
finally:
    conexion.close()