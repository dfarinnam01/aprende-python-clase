import requests


class APIEntradas:

    def __init__(self, base_url="http://localhost:5000/api"):
        self.base_url = base_url

    def create(self, data:dict):
        url = f"{self.base_url}/entradas"
        try:
            response = requests.post(url,json=data)
            return response.status_code, response.json()
        except:
            return 0, {"msg": "Se ha producido un error al conectar con el servidor"}
    def list_all(self):
        url = f"{self.base_url}/entradas"
        try:
            response = requests.get(url)
            return response.status_code, response.json()
        except:
            return 0, {"msg": "Se ha producido un error al conectar con el servidor"}

    def get(self, entrada_id):
        url = f"{self.base_url}/entradas/{entrada_id}"
        try:
            response = requests.get(url)
            return response.status_code, response.json()
        except:
            return 0, {"msg": "Se ha producido un error al conectar con el servidor"}