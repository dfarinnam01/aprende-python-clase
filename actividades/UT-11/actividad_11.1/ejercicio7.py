import requests

url = "http://httpbin.org/cookies"

cookies = {
    "usuario": "David",
    "session": "12345"
}

respuesta = requests.get(url, cookies=cookies)

print("Cookies enviadas:")
print(cookies)

print("\nRespuesta del servidor:")
print(respuesta.json())