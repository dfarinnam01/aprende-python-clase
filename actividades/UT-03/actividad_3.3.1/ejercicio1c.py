suma_notas=0
for i in range(5,0,-1):
    nota=(int(input(f"Asignatura {i+1}: ")))
    suma_notas=suma_notas + nota
print("Media de las notas es: ",suma_notas/5)