
total_segundos = int(input("Introduce el número total de segundos de la grabación: "))

horas = total_segundos // 3600

minutos = (total_segundos % 3600) // 60

segundos = total_segundos % 60

print("Horas completas:", horas)
print("Minutos completos restantes:", minutos)
print("Segundos restantes:", segundos)
