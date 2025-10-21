calificiones = []

for i in range(5):
    calificiones.append(int(input(f"Asignatura {i+1}: ")))
print(calificiones)
media = sum(calificiones)/len(calificiones)
print(media)