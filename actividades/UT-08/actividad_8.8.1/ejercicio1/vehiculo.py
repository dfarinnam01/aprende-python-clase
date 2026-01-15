class Vehiculo:
    def __init__(self, marca, modelo, color,numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numero_ruedas = numero_ruedas

    def tipo_vehiculo(self):
        print("Soy un vehiculo")