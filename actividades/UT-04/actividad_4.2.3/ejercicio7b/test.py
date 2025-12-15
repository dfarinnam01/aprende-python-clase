import random
class Test:
    __enunciados = [
        ("El sol es caliente.", "V"),
        ("El agua es seca.", "F"),
        ("Los perros son animales.", "V"),
        ("Los peces viven en el aire.", "F"),
        ("El cielo suele ser azul.", "V"),
        ("Las piedras pueden volar solas.", "F"),
        ("Las personas comen comida.", "V"),
        ("El fuego es frío.", "F"),
        ("Los pájaros pueden volar.", "V"),
        ("La leche es un tipo de bebida.", "V")
    ]

    def __init__(self):
        self.__preguntas=self.__enunciados.copy()
        random.shuffle(self.__preguntas)
        self.__preguntas=self.__preguntas[:5]
    def enunciado(self,n):
        return self.__preguntas[n][0]
    def verifica(self,respuestas):
        aciertos=0
        for i in range(len(self.__preguntas)):
            if self.__preguntas[i][0] in respuestas[i]:
                aciertos+=1
        return aciertos
    def informa_fallos(self,respuestas):
        aciertos=0
        fallos=[]
        for i in range(len(self.__preguntas)):
            if self.__preguntas[i][1] == respuestas[i]:
                aciertos+=1
            else:
                fallos.append(self.__preguntas[i][0])
        return aciertos,fallos
    def calcular_aciertos(self,aciertos):
        porcentaje=aciertos/5*100
        return porcentaje
if __name__=="__main__":
    test1=Test()
    respuestas = []

    for i in range(5):
        print(test1.enunciado(i))
        respuesta=input("Introduce (V o F): ")
        print()
        respuestas.append(respuesta)
    aciertos,fallos=test1.informa_fallos(respuestas)
    print(f"\nHas tenido {aciertos} aciertos")
    print(f"Tienes {test1.calcular_aciertos(aciertos)}% de aciertos\n")
    print("Preguntas falladas: ")
    for f in fallos:
        print(f)