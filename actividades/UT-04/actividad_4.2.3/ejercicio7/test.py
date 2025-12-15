import random
class Test:
    PREGUNTAS = [
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
    def get_pregunta_aleatoria(self):
        return random.choice(self.PREGUNTAS)
    def calcular_aciertos(self,aciertos):
        porcentaje=aciertos/5*100
        return porcentaje
