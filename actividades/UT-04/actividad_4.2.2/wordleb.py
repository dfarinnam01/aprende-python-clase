import random
ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[92m"
ANSI_ROJO = "\033[31m"
ANSI_AMARILLO = "\033[33m"
ANSI_CYAN = "\033[36m"
ANSI_RESET = "\033[0m"
palabras = ["perro"]

intentos = 0
print("¡¡¡BIENVENIDO A WORDLE!!!")

secreta = random.choice(palabras)

while intentos < 6:
    palabra_usuario = input("Introduce una palabra de 5 letras: ")
    while len(palabra_usuario) != 5:
        palabra_usuario = input("Introduce una palabra de 5 letras: ")

    c_letras = {}
    for letra in secreta:
        if letra in c_letras:
            c_letras[letra] += 1
        else:
            c_letras[letra] = 1

    # Creamos una copia para no modificar el original antes de la segunda pasada
    c_temp = c_letras.copy()
    resultado = [""] * 5

    # Primera pasada: letras verdes
    for i in range(5):
        if palabra_usuario[i] == secreta[i]:
            resultado[i] = ANSI_VERDE + palabra_usuario[i] + ANSI_RESET
            c_temp[palabra_usuario[i]] -= 1

    # Segunda pasada: amarillas y rojas
    for i in range(5):
        if resultado[i] == "":
            if palabra_usuario[i] in secreta and c_temp.get(palabra_usuario[i], 0) > 0:
                resultado[i] = ANSI_AMARILLO + palabra_usuario[i] + ANSI_RESET
                c_temp[palabra_usuario[i]] -= 1
            else:
                resultado[i] = ANSI_ROJO + palabra_usuario[i] + ANSI_RESET

    print("".join(resultado) + "\n")

    if palabra_usuario == secreta:
        print("¡¡¡FELICIDADES ACERTASTE LA PALABRA!!!")
        intentos = 6
    intentos += 1