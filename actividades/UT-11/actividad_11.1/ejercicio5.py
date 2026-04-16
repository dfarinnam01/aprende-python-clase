import requests

url = "https://www.google.com"

try:
    respuesta = requests.get(url, timeout=0.001)
    print("Respuesta recibida:", respuesta.status_code)

except requests.exceptions.Timeout:
    print("⏱️ Tiempo de espera agotado")

except requests.exceptions.RequestException as e:
    print("Error:", e)