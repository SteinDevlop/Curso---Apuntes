try:
    archivo = open("file_txt.txt","r", encoding="utf8")
    #formas de leer todas las lineas
    #Ciclo for

    #for linea in archivo:
    #    print(linea)

    #.readlines() (regresa una lista)
    
    #print(archivo.readlines())

    archivo2 = open("archivo2.txt","a")
    archivo2.write(archivo.read)
    archivo2.close()
    archivo.close()
except Exception as e:
    print(e)
