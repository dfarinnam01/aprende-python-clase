class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.color=""

    def acelerar(self,velocidad_acelererada):
        self.velocidad += velocidad_acelererada

    def frenar(self,velocidad_frenada):
        self.velocidad -= velocidad_frenada
    def cambiar_color(self,color):
        self.color = color

