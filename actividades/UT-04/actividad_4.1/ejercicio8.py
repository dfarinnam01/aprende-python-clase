importe_compra=int(input("Ingresa una cantidad de la compra: "))

if importe_compra<100:
    print("Sin descuento precio final: ",importe_compra)
elif importe_compra>100 and importe_compra<499:
    print("Descuento del 5% aplicado precio final:",importe_compra*0.95)
elif importe_compra>500 and importe_compra<999:
    print("Descuento del 10% aplicado precio final:", importe_compra * 0.90)
elif importe_compra>1000:
    print("Descuento del 15% aplicado precio final:", importe_compra * 0.85)