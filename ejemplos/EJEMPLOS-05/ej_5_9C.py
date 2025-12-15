class FakerNombre:
    __nombres = [
        "Ana", "Carlos", "Lucía", "Miguel", "Sofía",
        "Juan", "María", "Pedro", "Laura", "Diego",
        "Elena", "Pablo", "Carmen", "Javier", "Paula",
        "Andrés", "Isabel", "Raúl", "Natalia", "Fernando"
    ]

    def __init__(self):
        pass

    def __iter__(self):
        return iter(self.__nombres)

faker = FakerNombre()
iterador = iter(faker)
print(next(iterador))

print("------------")
for i in faker:
    print(i)