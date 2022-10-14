from modulo import Persona #del archivo, modulo, importamos la clase Persona
#si queremos poner todas las clases, usamos *
#si queremos importar mas clases, usamos el " , " como divisor

if __name__ == "__main__":
    print("Entrada".center(50,"-"))
    persona1 = Persona("Karla", "Gomez", 30)
    persona1.mostrar_detalle()
    print("Eliminacion de objetos".center(50,"-"))
    del persona1 #es raro usarlo, ya que en python existe un "recolector de basura"
    