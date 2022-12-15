from conexion import *
#el modulo se cambio de nombre a db
try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)"
    valores = ("Maria","Esparta","Mesperta@gmail.com")
    cursor.execute(sentencia,valores)
    sentencia = "UPDATE persona SET nombre=%s, apellido=%s,email=%s WHERE id_persona=%s"
    valores = ("Juan carlos","Juarez","jcjuares@gmail.com",1)
    cursor.execute(sentencia,valores)
    conexion.commit()
    print("Transaccion finalizada")
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, se hizo rollback: {e}")
finally:
    conexion.close()