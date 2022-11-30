try:
    archivo = open("file_txt.txt","w") #Abrimos el archivo en cuestion
    archivo.write("Agregamos informacion al archivo.txt")
    archivo.write("Otra linea je je je")
except Exception as e:
    print(e)
finally:
    archivo.close() #Cerramos la lectura del archivo en cuestion
    print("Archivo Cerrado")