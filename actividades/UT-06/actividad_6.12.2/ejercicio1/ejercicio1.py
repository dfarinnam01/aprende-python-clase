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
            entradas=f.readlines()
            #entradas=[linea.rstrip("\n") for linea in f.readlines()]
    except FileNotFoundError as e:
        f=open(FILENAME,"w",encoding="utf-8")
        f.close()
    except Exception as e:
        print("Se ha producido un error" +e)
    return entradas
def guardar(entrada):
    with open(FILENAME,"a",encoding="utf-8") as f:
        f.write(entrada+"\n")
    cargar_fichero()
def listar(entradas):
    for entrada in entradas:
        print(entrada)
def valida_entrada(entrada):
    return entrada.isdigit() and len(entrada)==5
contenido=cargar_fichero()
print(contenido)

guardar("00011")
contenido=cargar_fichero()
print(contenido)