nombres=[]
try:
    num=int(input("ingrese numero de nombres a introducir: "))
except ValueError:
    print("Introduce un numero valido")
for i in range(num):
    nombres.append(input(f"Introduce nombre {i+1}: "))
print("Nombres introducidos: ")
mostrar_nombres= " , ".join(nombres)
print(mostrar_nombres)