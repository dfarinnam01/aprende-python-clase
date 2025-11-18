frase="El perro de san roque no tiene rabo pero el perro de maricarmen si"
resultado=[x for x in frase.split() if x=="perro"]
print(resultado)

erres=[(i,x)for i,x in enumerate(frase) if x=="r"]
print(erres)