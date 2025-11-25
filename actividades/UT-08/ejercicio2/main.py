import Circulo as a
obj_circulo = a.Circulo(9)

print("El perimetro del circulo es:",obj_circulo.perimetro())
print("El area del circulo es: ",obj_circulo.area())

obj_circulo.set_altura(2)
print("El area del cilindro es: ",obj_circulo.area_Cilindro())

c1 = a.Circulo(1)
c2 = a.Circulo(1)

c1.cambiar_posicion((0,2))
c2.cambiar_posicion((2,2))

print("Se chocan los circulos" if c1.colision(c2)else "No se chocan los circulos")

for i in range(10):
    c2.cambiar_posicion((i,0))
    print(c1.posicion,c2.posicion,"Se chocan los circulos" if c1.colision(c2)else "No se chocan los circulos")