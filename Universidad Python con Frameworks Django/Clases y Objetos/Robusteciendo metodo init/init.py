class Persona:
    def __init__(self, nom,apel,ed, *valores, **terminos):
        self.nombre=nom
        self.apellido=apel
        self.edad=ed
        self.valores = valores
        self.terminos=terminos
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre}, {self.apellido}, {self.edad}, {self.valores},{self.terminos}")




persona1= Persona("juan","maria",23,"23124314",3,4,5,3,2,3,m="manzana",p="pera perosa")
persona1.mostrar_detalle()
persona2= Persona("Karla","Gomez",90)
persona2.mostrar_detalle()

Persona.mostrar_detalle(persona1)
Persona.mostrar_detalle(persona2)
#distinta forma de llamar al metodo

persona1.telefono="+570394932"
print(persona1.telefono)