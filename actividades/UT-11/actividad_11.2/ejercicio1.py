import requests
import re
import os

url = "https://www.hobbyconsolas.com/videojuegos/top-juegos/retro"

carpeta = "imagenes"
os.makedirs(carpeta, exist_ok=True)

response = requests.get(url)
html = response.text

patron = r"https://imagenes\.hobbyconsolas\.com/files/image_[^\"']+\.jpeg"

imagenes = re.findall(patron, html)

imagenes = list(set(imagenes))

print(f"Se encontraron {len(imagenes)} imágenes")


for i, img_url in enumerate(imagenes):
    try:
        img_data = requests.get(img_url).content

        nombre_archivo = f"{carpeta}/imagen_{i}.jpeg"

        with open(nombre_archivo, "wb") as f:
            f.write(img_data)

        print(f"Descargada: {nombre_archivo}")

    except Exception as e:
        print(f"Error con {img_url}: {e}")

