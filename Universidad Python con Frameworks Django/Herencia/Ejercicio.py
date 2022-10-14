"""
EJERCICIO:

Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo:
    def __init__(self,color,ruedas) -> str:
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return f"Contiene: {self.color}, {str(self.ruedas)}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self) -> str:
        return f"{super().__str__()}, {str(self.velocidad)} Km/Hr"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo) -> str:
        super().__init__(color, ruedas)
        self.tipo=tipo
    def __str__(self) -> str:
        return f"{super().__str__()}, {self.tipo}"

vehiculo = Vehiculo("Rojo",4)
print(vehiculo)
carro = Coche("Negro",4, 50)
print(carro)
bici = Bicicleta("Verde", 2,"ScreenShoot XV")
print(bici)