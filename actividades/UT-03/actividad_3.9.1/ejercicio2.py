salida=1
permitidos=[]
while salida!=0:
    asistente=input("Introduce numero de entrada (Salir con 0):")
    if asistente=="0":
        salida=0
    elif asistente not in permitidos:
        permitidos.append(asistente)
        print("Entrada valida")
    else:
        print("La entrada ya ha sido utilizada")