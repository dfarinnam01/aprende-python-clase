try:
    numero = int(input("Introduce un numero: "))
    print("El numero es: ", numero)
    print("Todo salió bien")
    a=3/0
except ValueError as e:
    print("Eso no es un número")
# except ZeroDivisionError as e:
#   print("No se puede dividir por 0",e )
except Exception as e:
    print("Error: ",e)

print("Fin del bloque")