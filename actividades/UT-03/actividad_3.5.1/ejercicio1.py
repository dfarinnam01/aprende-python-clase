tarjeta_clien=(input("Tienes Tarjeta de Cliente?(s/n) "))
if tarjeta_clien== "s":
    gastado=int(input("Gastado por Cliente?"))
    if gastado>100:
        print("Tiene derecho a una promocion")
else:
    print("Gracias igualmente!")
