c_entradas=int(input("Ingrese la cantidad de entradas que desea validar: "))
entradas_utilizadas=[]
for i in range(c_entradas):
    num_entrada = int(input("Introduce su numero de entrada: "))
    if num_entrada not in entradas_utilizadas:
        entradas_utilizadas.append(num_entrada)
        print("Acceso Permitido")
    else:
        print("Acceso Denegado")
