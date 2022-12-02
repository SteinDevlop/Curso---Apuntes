class ManejoArchivos:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    def __enter__(self):
        print(f"Obtenemos el recurso".center(50,"-"))
        self.nombre = open(self.nombre,"r", encoding="utf8")
        return self.nombre
    def __exit__(self,type_error,value_error,traze_error):
        print("Cerrando recurso".center(50,"-"))
        if self.nombre:
            self.nombre.close()
