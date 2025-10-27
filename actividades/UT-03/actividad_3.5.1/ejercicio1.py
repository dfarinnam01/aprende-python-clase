tarjeta_clien=bool(input("Tienes Tarjeta de Cliente?"))
if tarjeta_clien:
    gastado=int(input("Gastado por Cliente?"))
    if gastado>100:
        print("Tiene derecho a una promocion")
else:
    print("Gracias igualmente!")
