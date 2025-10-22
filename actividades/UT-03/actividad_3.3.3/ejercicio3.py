import math
nombre=input("Ingrese el nombre: ")

asignaturas=[]
notas=[]
for i in range(0,5):
    asignaturas.append(input("Ingrese el nombre de la asignatura: "))
    notas.append(int(input("Ingrese la nota de la asignatura: ")))

for i in range(0,5):
    print(asignaturas[i],":",notas[i])
media=sum(notas)/len(notas)
print(f"La media de las asignaturas es: {media}")