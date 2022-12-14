from conexion import *
#el modulo se cambio de nombre a db
try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)"
    valores = ("Maria","Esparta","Mesperta@gmail.com")
    cursor.execute(sentencia,valores)
    print("Transaccion finalizada")
    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f"Ocurrio un error, se hizo rollback{e}")
finally:
    conexion.close()