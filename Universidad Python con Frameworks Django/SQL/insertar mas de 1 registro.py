from conexion import *
import psycopg2

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
            valores = (
            ("Carlos","Lara","Clara@gmail.com"),
            ("Marco","Canton","Mcarnton@gmail.com"),
            ("Maria","Crisanta","Mcrisanta@gmail.com"),
            ("Casca","Canton","Ccanton@gmail.com"),
            ("Sancra","Marta","Smarta@gmail.com")
            )
            cursor.executemany(sentencia,valores)
            #conexion.commit()#guarda los cambios de forma automatica
            #.commit es inutil en  wth ya que los hace en automatico
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(e)
finally:
    conexion.close()