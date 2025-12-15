libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
try:
    print(next(marcapaginas))
    print(next(marcapaginas))
    print(next(marcapaginas))
    print(next(marcapaginas))
    print(next(marcapaginas))
except StopIteration:
    print("dale pa ya no hay mas paginas")
marcapaginas = iter(libro)
# for i in marcapaginas:
#     print(next(marcapaginas))
#esto no esta bien porque se haria de 2 en 2 nos compatible el next y el for
marcapaginas = iter(libro)
while True:
    try:
        print(next(marcapaginas))
    except StopIteration:
        print("dale pa no hay mas paginas")
        break