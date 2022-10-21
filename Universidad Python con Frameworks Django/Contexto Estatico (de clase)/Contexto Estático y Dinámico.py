class Miclase:
    variableDeClase = "String"
    def __init__(self,variable_instancia):
        self.variable_instancia=variable_instancia

    @classmethod
    def metodo_clase(cls):
        print(cls.variableDeClase)

    @staticmethod
    def metodoEstatico():
        print(Miclase.variableDeClase)

    def metodoInstancia(self):
        self.metodo_clase()
        self.metodoEstatico()
        print(self.variable_instancia)
        print(self.variableDeClase)

Miclase.metodo_clase()
objeto1 = Miclase("TEST")
objeto1.metodo_clase()
objeto1.metodoInstancia()