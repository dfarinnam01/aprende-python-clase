import random
intentos=0
acierto=False
num_random=random.randint(1,10)
while intentos<3 and not acierto:
    print(f"Intento {intentos+1}")
    num_introducido = int(input("Ingresa un numero: "))

    if num_introducido>num_random:
        print("El numero es menor al numero introducido")
    elif num_introducido<num_random:
        print("El numero es mayor al numero introducido")
    else:
       acierto=True

    intentos +=1

if acierto:
    print("\n!!!BIEN ACERTASTE EL NUMERO!!!")
else:
    print("\nNo acertaste el numero que era: ",num_random)