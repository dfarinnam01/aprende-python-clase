numeros_correctos=False
while not numeros_correctos:
    try:
        numero = int(input("Introduce un numero: "))
        numero2 = int(input("Introduce otro numero: "))

        numeros_correctos = True
    except Exception as e:
        print("Debe introducir dos numeros enteros")
suma = numero + numero2
print(suma)