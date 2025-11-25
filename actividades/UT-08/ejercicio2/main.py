import Circulo as a
obj_circulo = a.Circulo(9)

print("El perimetro del circulo es:",obj_circulo.perimetro())
print("El area del circulo es: ",obj_circulo.area())

obj_circulo.set_altura(2)
print("El area del cilindro es: ",obj_circulo.area_Cilindro())

c1 = a.Circulo(5)
c2 = a.Circulo(3)

c1.posicion = (0, 0)
c2.posicion = (6, 0)

print(c1.colision(c2))