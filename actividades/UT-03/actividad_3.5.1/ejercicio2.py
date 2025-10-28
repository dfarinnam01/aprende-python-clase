precio=float(input("Introduce precio del producto: "))
unidades=int(input("Introduce unidades del producto: "))
total=precio*unidades
descuento=0
if 50<=total<=100:
    descuento=5
elif 100<=total<=200:
    descuento=10
elif total>200:
    descuento=15

total_descuento=total-(total*descuento/100)
print("El precio del producto sin descuento: ",total)
print("El precio total del producto es: ",total_descuento)