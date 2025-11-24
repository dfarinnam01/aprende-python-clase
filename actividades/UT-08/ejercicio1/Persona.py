class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.dni=""

    def saludo(self):
        print("Hola " + self.nombre)

    def mayor_edad(self):
        return self.edad >= 18

    def cambia_dni(self,dni):
        self.dni = dni