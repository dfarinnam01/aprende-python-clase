calificaciones = [int(input("Nota 1: ")), int(input("Nota 2: ")), int(input("Nota 3: ")), int(input("Nota 4: ")), int(input("Nota 5: "))]

media = (calificaciones[0] + calificaciones[1] + calificaciones[2] + calificaciones[3] + calificaciones[4])/5
if media >=5:
     aprobado = True
else:
    aprobado = False

#aprobado = media >=5
print(calificaciones)
print(media)
print(aprobado)