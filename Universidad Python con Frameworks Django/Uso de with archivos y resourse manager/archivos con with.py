from ManejoDeArchivosjl import ManejoArchivos
with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())