class Miclase:
    variableDeClase = "String"
    def __init__(self,variable_instancia):
        self.variable_instancia=variable_instancia
    
    @classmethod
    #cls es para abrevias class, no debe usar class directamente
    def metodo_clase(cls):
        print(cls.variableDeClase)
Miclase.metodo_clase()