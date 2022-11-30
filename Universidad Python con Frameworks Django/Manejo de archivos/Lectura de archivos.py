try:
    archivo = open("file_txt.txt","r", encoding="utf8")
    #print(archivo.read())
    #.read lee todo el archivo si lo dejamos en blanco
    #podemos especificar cuantos caracteres leer
    print(archivo.read(3))
    #Podemos leer lineas completas
    print(archivo.readline())
except Exception as e:
    print(e)
