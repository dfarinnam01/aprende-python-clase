importe_compra=int(input("Ingresa una cantidad de la compra: "))

if importe_compra<100:
    dto=0
elif importe_compra>100 and importe_compra<499:
    dto=0.95
elif importe_compra>500 and importe_compra<999:
    dto=0.90
elif importe_compra>1000:
   dto=0.80
print("Descuento del 10% aplicado precio final:", importe_compra * dto)