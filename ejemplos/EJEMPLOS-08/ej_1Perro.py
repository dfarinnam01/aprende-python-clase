class Perro:
    def __init__(self):
        self.nombre = ""
        self.raza=""
    def cambia_nombre(self,nombre):
        self.nombre = nombre
if __name__ == '__main__':
    perro = Perro()
    perro.cambia_nombre("Pepe")
    print(f"Nombre: {perro.nombre}")