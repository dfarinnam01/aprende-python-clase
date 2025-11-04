nombre_archivo = __file__
print(nombre_archivo)
f = open(nombre_archivo , "r")
contenido = f.read()
print(contenido)
f.close()