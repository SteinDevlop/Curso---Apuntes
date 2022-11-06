class Miclase:
    variableDeClase = "String"
    def __init__(self,variable_instancia):
        self.variable_instancia=variable_instancia
    
    @staticmethod
    def metodoEstatico():
        print(Miclase.variableDeClase)
#        print(variableDeClase), no se puede porque es un contexto estatico; para acceder a la variable debemos usar el nombre de clase
Miclase.metodoEstatico()
