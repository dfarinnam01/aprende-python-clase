print("Fecha 1")
print("="*50)
dia=input("Ingresa el dia: ")
mes=input("Ingresa el mes: ")
anyo=input("Ingresa el año: ")
print("Fecha 2")
print("="*50)
dia2=input("Ingresa el dia: ")
mes2=input("Ingresa el mes: ")
anyo2=input("Ingresa el año: ")

if anyo>anyo2:
    print("Fecha 1 mayor")
elif anyo2>anyo:
    print("Fecha 2 mayor")
elif anyo==anyo2:
    if mes>mes2:
        print("Fecha 1 mayor")
    elif mes<mes2:
        print("Fecha 2 mayor")
    elif mes==mes2:
        if dia>dia2:
            print("Fecha 1 mayor")
        else:
            print("Fecha 2 mayor")