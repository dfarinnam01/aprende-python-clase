import requests

url = "https://www.example.com"

respuesta = requests.get(url)

print("TEXT:")
print(respuesta.text[:500])  # solo un trozo

print("\nCONTENT:")
print(respuesta.content[:200])  # bytes