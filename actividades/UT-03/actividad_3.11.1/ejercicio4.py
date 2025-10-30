fecha="24/1/2025"
fecha_separada=fecha.split("/")

fecha2="24/2/2025"
fecha_separada2=fecha2.split("/")

if fecha_separada[2] < fecha_separada2[2]:
    menor = fecha
elif fecha_separada2[2] > fecha_separada[2]:
    menor = fecha2
else:
    if fecha_separada[1] < fecha_separada2[1]:
        menor = fecha
    elif fecha_separada[1] > fecha_separada2[1]:
        menor = fecha2
    else:
        if fecha_separada[0] < fecha_separada2[0]:
            menor = fecha
        elif fecha_separada[0] > fecha_separada2[0]:
            menor = fecha2
        else:
            menor = "Ambas fechas son iguales."
print("La fecha menor es:", menor)