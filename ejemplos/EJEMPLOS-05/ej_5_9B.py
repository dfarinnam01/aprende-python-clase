class MiClase:
    def __init__(self, items):
        self.lista = items

    def __iter__(self):
        return iter(self.lista)

miobjeto = MiClase([5,3,5])
iterador = iter(miobjeto)
print(next(iterador))

print("------------")
for i in miobjeto:
    print(i)