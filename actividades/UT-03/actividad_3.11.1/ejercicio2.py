cadena = "    Python,Java   ,C   "
cadena_sin_espacios=cadena.strip().replace(" ","")
lista= cadena_sin_espacios.split(",")
print(lista)