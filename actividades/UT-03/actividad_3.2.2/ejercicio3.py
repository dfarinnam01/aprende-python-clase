horas = 5
minutos = 123

while(minutos>=60):
    horas=horas+1
    minutos=minutos-60
print(f"La pelicula dura {horas} horas y {minutos} minutos")

duracion_pelicula = (horas*60)+minutos
print(f"La pelicula dura {duracion_pelicula} minutos")