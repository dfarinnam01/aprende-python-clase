anyo=int(input("Introduce un año: "))

if anyo%4==0 and anyo%100!=0 or anyo%400==0:
    print("Año bisiesto")
else:
    print("Año no bisiesto")