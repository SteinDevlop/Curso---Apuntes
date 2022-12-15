from conexion import *
#el modulo se cambio de nombre a db
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)"
            valores = ("Carla","Carhan","Carka@gmail.com")
            cursor.execute(sentencia,valores)
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s,email=%s WHERE id_persona=%s"
            valores = ("Juan carlos","Juarez","jcjuares@gmail.com",1)
            cursor.execute(sentencia,valores)
except Exception as e:
    print(f"Ocurrio un error, rollback aplicado automatico {e}")
finally:
    print("Transaccion finalizada")
    conexion.close()