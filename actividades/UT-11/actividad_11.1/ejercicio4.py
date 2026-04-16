import requests

url = "https://api.github.com"

respuesta = requests.get(url)

try:
    datos = respuesta.json()

    print("JSON COMPLETO:")
    print(datos)

    print("\nCLAVES:")
    for clave in datos:
        print(clave, "->", datos[clave])

except ValueError:
    print("La respuesta no es JSON")