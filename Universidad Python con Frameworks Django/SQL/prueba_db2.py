import psycopg2
conexion = psycopg2.connect(
user="postgres",
password="admin",
host="127.0.0.1",
port="5432",
database="pyUni_db"
)
#segun la documentacion, esta es la mejor manera de llamar y cerrar la db
try:

    with conexion:
        with conexion.cursor() as cursor:
            sentence = "SELECT * FROM persona"
            cursor.execute(sentence)
            registros = cursor.fetchall()
            print(registros)
except Exception as exept:
    print(f"Ocurrio un error: {exept}")
finally:
    conexion.close()