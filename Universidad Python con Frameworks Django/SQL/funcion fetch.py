import psycopg2
conexion = psycopg2.connect(
user="postgres",
password="admin",
host="127.0.0.1",
port="5432",
database="pyUni_db"
)
try:

    with conexion:
        with conexion.cursor() as cursor:
            sentence = "SELECT * FROM persona WHERE id_persona =%s"#parametro posicional %s
            id_persona = input("valor id: ")
            cursor.execute(sentence,(id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as exept:
    print(f"Ocurrio un error: {exept}")
finally:
    conexion.close()