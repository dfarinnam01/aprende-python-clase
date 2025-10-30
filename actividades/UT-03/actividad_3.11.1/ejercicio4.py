fecha1 = input("Introduce la primera fecha (dia/mes/año): ")
fecha2 = input("Introduce la segunda fecha (dia/mes/año): ")

dia1 = int(fecha1.split("/")[0])
mes1 = int(fecha1.split("/")[1])
anio1 = int(fecha1.split("/")[2])

dia2 = int(fecha2.split("/")[0])
mes2 = int(fecha2.split("/")[1])
anio2 = int(fecha2.split("/")[2])

if anio1 < anio2:
    menor = fecha1
elif anio1 > anio2:
    menor = fecha2
else:
    if mes1 < mes2:
        menor = fecha1
    elif mes1 > mes2:
        menor = fecha2
    else:
        if dia1 < dia2:
            menor = fecha1
        elif dia1 > dia2:
            menor = fecha2
        else:
            menor = "Ambas fechas son iguales."

# Mostrar el resultado
print("La fecha menor es:", menor)
