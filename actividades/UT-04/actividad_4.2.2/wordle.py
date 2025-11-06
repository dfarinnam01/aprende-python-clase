import random
ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[92m"
ANSI_ROJO = "\033[31m"
ANSI_AMARILLO = "\033[33m"
ANSI_CYAN = "\033[36m"
ANSI_RESET = "\033[0m"
palabras = ["lejos"]


c_letras = {}
secreta = random.choice(palabras)
intentos=0
print("¡¡¡BIENVENIDO A WORDLE!!!")
while intentos <6:
    palabra_usuario=input("Introduce una palabra de 5 letras: ")
    while len(palabra_usuario) !=5:
        palabra_usuario = input("Introduce una palabra de 5 letras: ")

    for letra in secreta:
        if letra in c_letras:
            c_letras[letra] += 1
        else:
            c_letras[letra] = 1

    print(c_letras)

    for i in range(len(palabra_usuario)):
        if palabra_usuario[i] == secreta[i]:
            c_letras[palabra_usuario[i]] -=1
            print(ANSI_VERDE,palabra_usuario[i],ANSI_RESET,end="")
        elif palabra_usuario[i] != secreta[i] and palabra_usuario[i] in secreta and c_letras[palabra_usuario[i]] > 0:
            c_letras[palabra_usuario[i]] -= 1
            print(ANSI_AMARILLO, palabra_usuario[i], ANSI_RESET, end="")
        else:
            print(palabra_usuario[i],end="")
    print("\n")
    if palabra_usuario == secreta:
        print("¡¡¡FELICIDADES ACERTASTE LA PALABRA")
        intentos=6
    intentos=intentos+1