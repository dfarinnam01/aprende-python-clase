tarjeta_clien=(input("Tienes Tarjeta de Cliente?(s/n) "))
gastado = int(input("Gastado por Cliente?"))
if tarjeta_clien== "s":
    print("Tiene derecho a una promocion")
else:
    if gastado>100:
        print("Tiene derecho a una promocion")
