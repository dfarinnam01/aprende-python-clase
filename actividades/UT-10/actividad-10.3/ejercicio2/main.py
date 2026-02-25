import csv

# Contadores generales
total_usuarios = 0

moderada = 0
severa = 0

moderada_hombres = 0
moderada_mujeres = 0

severa_hombres = 0
severa_mujeres = 0

# Para relación ansiedad vs tiempo pantalla
rangos_ansiedad = {
    "0-4": {"suma": 0, "contador": 0},
    "5-9": {"suma": 0, "contador": 0},
    "10-14": {"suma": 0, "contador": 0},
    "15-18": {"suma": 0, "contador": 0},
    "19-21": {"suma": 0, "contador": 0},
}

# Para tipo contenido vs ansiedad
contenido_ansiedad = {}

# Para late night vs ansiedad
late_night_ansiedad = {0: {"suma": 0, "contador": 0},
                       1: {"suma": 0, "contador": 0}}


with open("social_media_mental_health.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        total_usuarios += 1

        genero = fila["Gender"]
        severidad = fila["GAD_7_Severity"]
        ansiedad_score = int(fila["GAD_7_Score"])
        tiempo_pantalla = float(fila["Daily_Screen_Time_Hours"])
        tipo_contenido = fila["Dominant_Content_Type"]
        late_night = int(fila["Late_Night_Usage"])

        # 1️⃣ Moderados y severos
        if severidad.lower() == "moderate":
            moderada += 1
            if genero.lower() == "male":
                moderada_hombres += 1
            else:
                moderada_mujeres += 1

        if severidad.lower() == "severe":
            severa += 1
            if genero.lower() == "male":
                severa_hombres += 1
            else:
                severa_mujeres += 1

        # 2️⃣ Ansiedad vs tiempo pantalla (por rangos score)
        if 0 <= ansiedad_score <= 4:
            rango = "0-4"
        elif 5 <= ansiedad_score <= 9:
            rango = "5-9"
        elif 10 <= ansiedad_score <= 14:
            rango = "10-14"
        elif 15 <= ansiedad_score <= 18:
            rango = "15-18"
        else:
            rango = "19-21"

        rangos_ansiedad[rango]["suma"] += tiempo_pantalla
        rangos_ansiedad[rango]["contador"] += 1

        # 3️⃣ Tipo contenido vs ansiedad (media ansiedad)
        if tipo_contenido not in contenido_ansiedad:
            contenido_ansiedad[tipo_contenido] = {"suma": 0, "contador": 0}

        contenido_ansiedad[tipo_contenido]["suma"] += ansiedad_score
        contenido_ansiedad[tipo_contenido]["contador"] += 1

        # 4️⃣ Late night vs ansiedad
        late_night_ansiedad[late_night]["suma"] += ansiedad_score
        late_night_ansiedad[late_night]["contador"] += 1


# ==========================
# RESULTADOS
# ==========================

print("\n--- USUARIOS CON ANSIEDAD ---")
print(f"Moderada: {moderada} ({moderada/total_usuarios*100:.2f}%)")
print(f"Severa: {severa} ({severa/total_usuarios*100:.2f}%)")

print("\n--- MODERADA POR GÉNERO ---")
if moderada > 0:
    print(f"Hombres: {moderada_hombres} ({moderada_hombres/moderada*100:.2f}%)")
    print(f"Mujeres: {moderada_mujeres} ({moderada_mujeres/moderada*100:.2f}%)")

print("\n--- SEVERA POR GÉNERO ---")
if severa > 0:
    print(f"Hombres: {severa_hombres} ({severa_hombres/severa*100:.2f}%)")
    print(f"Mujeres: {severa_mujeres} ({severa_mujeres/severa*100:.2f}%)")


print("\n--- Ansiedad vs Tiempo Pantalla ---")
for rango, datos in rangos_ansiedad.items():
    if datos["contador"] > 0:
        media = datos["suma"] / datos["contador"]
        print(f"{rango} => {media:.2f}")


print("\n--- Tipo contenido vs Ansiedad ---")
for tipo, datos in contenido_ansiedad.items():
    media = datos["suma"] / datos["contador"]
    print(f"{tipo} => {media:.2f}")


print("\n--- Late Night Usage vs Ansiedad ---")
for clave, datos in late_night_ansiedad.items():
    if datos["contador"] > 0:
        media = datos["suma"] / datos["contador"]
        estado = "No" if clave == 0 else "Sí"
        print(f"Late Night ({estado}) => {media:.2f}")
