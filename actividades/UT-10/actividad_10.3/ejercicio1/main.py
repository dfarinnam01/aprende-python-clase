import csv


suma_duracion = 0
suma_paginas = 0
suma_acciones = 0
suma_valor = 0
suma_clase = 0

contador = 0
cw=0
cl=0
cmac=0

with open("usuarios_win_mac_lin.csv", newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)

    next(lector)

    for fila in lector:
        suma_duracion += float(fila[0])
        suma_paginas += float(fila[1])
        suma_acciones += float(fila[2])
        suma_valor += float(fila[3])
        suma_clase += float(fila[4])
        if float(fila[4])==0:
            cw += 1
        elif float(fila[4])==2:
            cl+=1
        else:
            cmac+=1

        contador += 1

media_duracion = suma_duracion / contador
media_paginas = suma_paginas / contador
media_acciones = suma_acciones / contador
media_valor = suma_valor / contador
media_clase = suma_clase / contador

porcentaje_windows=(cw*100/contador)
porcentaje_linux=(cl*100/contador)
porcentaje_mac=(cmac*100/contador)

print("Media duración:", media_duracion)
print("Media páginas:", media_paginas)
print("Media acciones:", media_acciones)
print("Media valor:", media_valor)
print("Media clase:", media_clase)

print(f"\nPorcentaje de uso en Windows: {porcentaje_windows:.2f}%")
print(f"Porcentaje de uso en Linux: {porcentaje_linux:.2f}%")
print(f"Porcentaje de uso en Mac: {porcentaje_mac:.2f}%")

