x=[10,20,30]
def mueve(entrada,*valor):
    for v in valor:
        entrada.append(v)
    print(entrada)
    lista=[]
    for v in entrada:
        lista.append(v)
    #lista = entrada.copy()
    entrada.clear()
    return lista
lista=mueve(x,1,2,3)
print(lista)
print(x)