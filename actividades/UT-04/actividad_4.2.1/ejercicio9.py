import random
intentos=0
acierto=False
num_random=random.randint(1,100)
while not acierto:
    num_introducido = int(input("Ingresa un numero: "))

    if num_introducido>num_random:
        print("El numero es menor al numero introducido")
    elif num_introducido<num_random:
        print("El numero es mayor al numero introducido")
    else:
       acierto=True

    intentos +=1
print(f"\n¡¡¡ACERTASTE!!! Has necesitado {intentos} intentos")
