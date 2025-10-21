calificiones = []

calificiones.append(int(input("Asignatura 1: ")))
calificiones.append(int(input("Asignatura 2: ")))
calificiones.append(int(input("Asignatura 3: ")))
calificiones.append(int(input("Asignatura 4: ")))
calificiones.append(int(input("Asignatura 5: ")))

media = sum(calificiones)/len(calificiones)
print(media)