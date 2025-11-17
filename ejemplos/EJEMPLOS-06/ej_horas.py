from datetime import datetime

FECHA_SALIDA = datetime(2025, 11, 10)

fecha_actual = datetime.now()


dias_transcurridos = (fecha_actual - FECHA_SALIDA).days

horas = int(input("Ingrese las horas jugadas en total: "))
minutos = int(input("Ingrese los minutos jugados en total: "))

while minutos>59 or minutos<0:
    minutos = int(input("Ingrese los minutos en total: "))

promedio_horas = horas / dias_transcurridos
horas_promedio = int(promedio_horas)
minutos_promedio = int((promedio_horas - horas_promedio) * 60)

print(f"Han pasado {dias_transcurridos} días desde la salida del juego.")
print(f"Promedio de juego por día: {horas_promedio} horas con {minutos_promedio} minutos")
