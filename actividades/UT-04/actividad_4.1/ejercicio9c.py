import random

intentos=0

num_random=random.randint(1,10)
num_introducido=0

while intentos<3 and num_introducido!=num_random:
    print(f"Intento {intentos+1}")
    num_introducido = int(input("Ingresa un numero: "))

    if num_introducido>num_random:
        print("El numero es menor al numero introducido")
    elif num_introducido<num_random:
        print("El numero es mayor al numero introducido")

    intentos=intentos+1

if num_introducido==num_random:
    print("\n!!!BIEN ACERTASTE EL NUMERO!!!")
else:
    print("\nNo acertaste el numero que era: ",num_random)