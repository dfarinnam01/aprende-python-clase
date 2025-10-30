fecha="24/1/2025"
fecha_separada=fecha.split("/")

fecha2="24/2/2025"
fecha_separada2=fecha2.split("/")
if(len(fecha_separada2)==3) and (len(fecha_separada2)==3):
    fecha_numerica1=int(fecha_separada[2])*10000+ int(fecha_separada[1])* 100 + int(fecha_separada[0])
    fecha_numerica2=int(fecha_separada2[2])*10000+ int(fecha_separada2[1])* 100 + int(fecha_separada2[0])

    if fecha_numerica1>fecha_numerica2:
        print("Fecha 1 es mayor que Fecha 2")
    elif fecha_numerica2>fecha_numerica1:
        print("Fecha 2 es mayor que Fecha 1")
    else:
        print("Ambas fechas son iguales")