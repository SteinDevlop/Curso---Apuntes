try:
    archivo = open("file_txt.txt","w", encoding="utf8")
    archivo.write("Agregamos informacion al archivo.txt\n")
    archivo.write("Otra linea je je je")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("Archivo Cerrado")