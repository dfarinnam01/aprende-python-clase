def nueva_entrada():
    pass
def consulta_entrada():
    pass
def listados_entrada():
    pass

FILENAME="entradas.txt"
def menu():
    print("1. Entrada")
    print("2. Consulta")
    print("3. Listados")
    print("0. Salir")
    opcion=-1
    while not opcion in [1,2,3,0]:
        opcion=int(input("Introduce una opción: "))
    return opcion

def cargar_fichero():
    try:
        entradas=[]
        with open(FILENAME,"r",encoding="utf-8") as f:
            #entradas=f.readlines()
            entradas=[linea.rstrip("\n") for linea in f.readlines()]
    except FileNotFoundError as e:
        f=open(FILENAME,"w",encoding="utf-8")
        f.close()
    except Exception as e:
        print("Se ha producido un error" +e)
    return entradas

def guardar(entrada):
    with open(FILENAME,"a",encoding="utf-8") as f:
        f.write(entrada+"\n")

def listar(entradas):
    for entrada in entradas:
        print(entrada)

# Muestra si existe la entrada y la posicion en la que se encuentra
def consultar(entradas, entrada):
    if not entrada:
        return
    pos=0
    while pos<len(entradas) and entradas[pos]!=entrada :
        pos=pos+1
    if pos<len(entradas):
        print("Entrada encontrada en la posicion: ",pos)
    else:
        print("Entrada no encontrada")

    # pos=-1
    # for i in range(len(entradas)):
    #     if entradas[i]==entrada:
    #         pos=i
    #         break
    # if pos!=-1:
    #     print("Entrada encontrada en la posicion: ",pos)
    # else:
    #     print("Entrada no encontrada")

    # encontrado=False
    # for index,e in enumerate(entradas):
    #     if e==entrada:
    #         encontrado=True
    # if encontrado:
    #     print("Entrada encontrada en la posicion: ",index)
    # else:
    #     print("Entrada no encontrada")


    # pos=next((index for index,e in enumerate(entradas) if entrada==e),None)
    # if pos is not None :
    #     print("Entrada encontrada en la posicion: ",pos)
    # else:
    #     print("Entrada no encontrada")
    #
def valida_entrada(entrada):
    return entrada.isdigit() and len(entrada)==5

#TESTS
# contenido=cargar_fichero()
# print(contenido)
#
# guardar("00011")
# contenido=cargar_fichero()
# print(contenido)

if __name__ == "__main__":
    entradas=cargar_fichero()
    opcion=""
    while opcion !=0:
        opcion=menu()
        match opcion:
            case 1:
                entrada=""
                while not valida_entrada(entrada):
                    entrada=input("Introduce una entrada: ")
                guardar(entrada)
                print("Entrada guardada")
                entradas.append(entrada)
            case 2:
                entrada = ""
                while not valida_entrada(entrada):
                    entrada = input("Introduce una entrada: ")
                consultar(entradas, entrada)
            case 3:
                listar(entradas)
