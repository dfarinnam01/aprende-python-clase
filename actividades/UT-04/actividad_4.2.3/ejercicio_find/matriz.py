import random


class Matriz:
    __matriz = [
        (1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 16)
    ]

    def buscar(self):
        num=int(input("Ingresa un numero a buscar: "))
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz)):
                if self.__matriz[i][j] == num:
                    return i, j
        return "No encontrado"

    def random_matriz(self):
        matriz = []
        for i in range(5):
            fila = []
            for j in range(5):
                fila.append(random.randint(1, 10))
            matriz.append(fila)
        print(matriz)
if __name__ == '__main__':
    matriz = Matriz()
    print(matriz.buscar())
    matriz.random_matriz()