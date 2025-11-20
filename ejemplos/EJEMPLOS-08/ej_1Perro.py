class Perro:
    def __init__(self,nombre,raza):
        self.nombre = ""
        self.raza=""
    def cambia_nombre(self,nombre):
        self.nombre = nombre
if __name__ == '__main__':
    perro = Perro("Pepe","Chucho")
    perro.cambia_nombre("Tomi")
    print(f"Nombre: {perro.nombre}")
    print(f"Raza: {perro.raza}")

#Añadir un metodo