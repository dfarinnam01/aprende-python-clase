class Circulo:
    PI=3.14
    def __init__(self,radio):
        self.radio=radio
        self.altura=0

    def area(self):
        return self.radio*self.radio*self.PI

    def perimetro(self):
        return self.radio*self.PI*2

    def set_altura(self,altura):
        self.altura=altura

    def area_Cilindro(self):
        return self.area()*self.altura
    def colision(self,circulo):
        pass
    #Si la hipotenusa es menor a la suma de los lados estan colisionando
    #lado del triangulo: x2-x1 y2-y1 y hacer pitagoras sacamos la hipotenusa