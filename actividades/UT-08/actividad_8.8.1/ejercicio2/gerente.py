from empresario import Empresario
class Gerente(Empresario):
    def __init__(self,nombre,salario,departamento):
        super().__init__(nombre,salario)
        self.departamento = departamento
    def mostrar_info(self):
        print("Nombre: ",self.nombre)
        print("Salario: ",self.salario)
        print("Departamento: ",self.departamento)