from test import Test

if __name__=="__main__":
    obj_test=Test()
    correcta=0
    print("PREGUNTAS TIPO TEST")

    for i in range(0,5):
        pregunta=obj_test.get_pregunta_aleatoria()
        print(pregunta[0])
        respuesta=input("V o F: ")
        if respuesta == pregunta[1]:
            correcta=correcta+1
    print(f"Tienes el {obj_test.calcular_aciertos(correcta)}% de aciertos")