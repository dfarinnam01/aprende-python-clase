asignaturas=[]
suma=0
nombre=input("Ingrese el nombre: ")

for i in range(0,2):
    asignatura=input("Ingrese asignatura: ")
    nota=float(input("Ingrese nota de la asignatura: "))
    asignaturas.append([asignatura,nota])

for asignatura in asignaturas:
    print(f"{asignatura[0]}: {asignatura[1]}")
    suma=suma+asignatura[1]
media = suma/len(asignaturas)
print(media)

