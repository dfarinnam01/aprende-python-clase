def suma(*args):
    suma = 0
    for arg in args:
        suma= suma + arg
    return suma
print(suma(1,2,3,1))