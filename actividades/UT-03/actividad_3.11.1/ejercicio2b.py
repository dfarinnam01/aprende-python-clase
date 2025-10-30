cadena = "    Python,Java   ,C   "
palabras = cadena.strip().split(',')

for i in range(len(palabras)):
    palabras[i] = palabras[i].strip()

print(palabras)
