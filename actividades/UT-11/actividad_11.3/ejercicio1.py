import requests
from bs4 import BeautifulSoup
import os
import time

BASE_URL = "https://pokemondb.net"
LIST_URL = "https://pokemondb.net/pokedex/all"

# Carpeta donde guardar imágenes
os.makedirs("pokemon_imgs", exist_ok=True)

# 1️⃣ Obtener lista de pokémon
response = requests.get(LIST_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Buscar enlaces a cada pokémon
links = soup.select("a.ent-name")

pokemon_urls = []

for link in links:
    nombre = link.text.strip().lower()
    url = BASE_URL + link["href"]
    pokemon_urls.append((nombre, url))

print(f"Total pokémon encontrados: {len(pokemon_urls)}")

# 2️⃣ Entrar en cada página y descargar imagen
for nombre, url in pokemon_urls:
    print(f"Procesando: {nombre}")

    res = requests.get(url)
    soup_poke = BeautifulSoup(res.text, "html.parser")

    # OPCIÓN 1 (más fácil): construir la URL directamente
    img_url = f"https://img.pokemondb.net/artwork/avif/{nombre}.avif"

    # OPCIÓN 2 (más robusta): buscar la imagen real en la página
    # img_tag = soup_poke.select_one(".figure img")
    # img_url = img_tag["src"]

    # Descargar imagen
    img_data = requests.get(img_url).content

    with open(f"pokemon_imgs/{nombre}.avif", "wb") as f:
        f.write(img_data)

    # Pausa para no saturar el servidor
    time.sleep(0.2)

print("Descarga completada.")