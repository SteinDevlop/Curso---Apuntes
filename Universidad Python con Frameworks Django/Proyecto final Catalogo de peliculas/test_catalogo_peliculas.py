from Dominio.pelicula import *
from Servicio.catalogoDepeliculas import * 
Option = None
while Option != 4:
    print("".center(50,"-"))
    print("""Opciones de ejecucion:
1) Agregar peliculas.
2) Listar peliculas existentes.
3) Eliminar archivo de la pelicula.
4) Salir.""")
    print("".center(50,"-"))

    try:
        Option = int(input("Seleccione la opcion (1-4): "))
    except ValueError as ve:
        print(f"Hubo un error en el ingreso de datos.")
        print(f"Seleccione unicamente en valor numerica de la opcion 1 hasta la 4.")
        exit()
    except Exception as e:
        print(f"Hubo un error: {type(e)}")
        exit()

    if Option == 1:
        pelicula = str(input("Nombre de la pelicula: "))
        pelicula = Pelicula(pelicula)
        Catalogo_De_Peliculas.agregar_pelicula(pelicula)
    elif Option == 2:
        print("Listado de peliculas".center(50,"-"))
        try:
            Catalogo_De_Peliculas.listar_peliculas()
        except FileNotFoundError as fnfe:
            print(f"Ingrese una pelicula para continuar.")
        except Exception as e:
            print(f"Error encontrado {type(e)}")
        print("".center(50,"-"))
    elif Option == 3:
        try:
            Catalogo_De_Peliculas.eliminar_archivo()
        except WindowsError as windows:
            print("No se ha creado el archivo en cuestion")
            with open('peliculas.txt', 'w'):
                pass
        except Exception as e:
            print(e)