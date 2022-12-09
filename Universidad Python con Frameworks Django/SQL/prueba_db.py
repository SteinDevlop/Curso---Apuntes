import psycopg2
conexion = psycopg2.connect(
user="postgres",
password="admin",
host="127.0.0.1",
port="5432",
database="pyUni_db"
)
cursor = conexion.cursor()
sentence = "SELECT * FROM persona"
cursor.execute(sentence)
registros = cursor.fetchall()
print(registros)
cursor.close()
conexion.close()