import math
class Rectangulo:
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        self.diagonal=0
    def area(self):
        return self.ancho * self.alto

    def set_diagonal(self):
        self.diagonal = math.sqrt(self.ancho**2 + self.alto**2)

