import requests

urls = [
    "https://www.amazon.es",
    "https://www.google.com",
    "https://estawebnoexiste123456.com"
]

for url in urls:
    try:
        respuesta = requests.get(url)
        print(f"{url} -> Código: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url} -> Error: {e}")