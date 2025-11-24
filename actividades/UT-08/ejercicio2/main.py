import Circulo as a
obj_circulo = a.Circulo(9)

print("El perimetro del circulo es:",obj_circulo.perimetro())
print("El area del circulo es: ",obj_circulo.area())

obj_circulo.set_altura(2)
print("El area del cilindro es: ",obj_circulo.area_Cilindro())