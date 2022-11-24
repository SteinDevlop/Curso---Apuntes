from Orden import *
from Computadora import *
from Entrada import *
from Monitor import *

if __name__ == "__main__":
    teclado1 = Teclado("USB","HP")
    teclado2 = Teclado("SSR","Genius")
    raton1 = Raton("USB","Acer")
    raton2 = Raton("USB","HP")
    monitor1 = Monitor("Compumax",32)
    monitor2 = Monitor("LG",14)

    teclado3 = Teclado("Wi-Fi","Lg")
    raton3 = Raton("USB","ZEr-Cops")
    monitor3 = Monitor("National Gouverment Colombian",122)
    computadora1 = Computadora("HP",monitor1,teclado1,raton1)
    pc2 = Computadora("Fabrica COL-ECOLOS",monitor1,teclado2,raton2)
    computadora3 = Computadora("National Middle-Worker PC",monitor3,teclado3,raton3)
    computadoras1 = [computadora1,pc2]
    orden1 = Orden(computadoras1)
    print(orden1)
    orden1.agregarComputadora(computadora3)
    print(orden1)