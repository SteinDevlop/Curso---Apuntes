with open("prueba.txt","r",encoding="utf8") as archivo: #with se ejecuta de manera automatica, y lo abre y al finalizar, lo cierra sin el finally
    print(archivo.readlines())