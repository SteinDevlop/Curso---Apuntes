import psycopg2 as db
try:
    conexion = db.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='pyUni_db')
except Exception as e:
    print(f"Error al conectar base de datos, Detalle: {type(e)}")