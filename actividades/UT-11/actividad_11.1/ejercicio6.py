import requests

url = "http://httpbin.org/get"

parametros = {
    "nombre": "David",
    "edad": 22
}

respuesta = requests.get(url, params=parametros)

print("URL final:")
print(respuesta.url)

print("\nRespuesta JSON:")
print(respuesta.json())