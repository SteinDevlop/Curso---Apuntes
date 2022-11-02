from ClaseEmpleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, sueldo,departamento) -> None:
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    def __str__(self) -> str:
        return f"Departamento: {self.departamento} , {super().__str__()}"