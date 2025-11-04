nota=float(input("Ingresa una nota (0-10): "))

while nota <0 or nota >10:
    nota=float(input("Ingresa una nota (0-10): "))

if nota <5:
    print("Suspenso")
elif nota >=5 and nota <6.9:
    print("Aprobado")
elif nota >=7 and nota <8.9:
    print("Notable")
else:
    print("Sobresaliente")