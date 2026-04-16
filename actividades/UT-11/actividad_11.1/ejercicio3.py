import requests

url = "https://api.github.com"

respuesta = requests.get(url)

print("HEADERS COMPLETOS:")
print(respuesta.headers)

print("\nCLAVE - VALOR:")
for clave, valor in respuesta.headers.items():
    print(f"{clave} -> {valor}")