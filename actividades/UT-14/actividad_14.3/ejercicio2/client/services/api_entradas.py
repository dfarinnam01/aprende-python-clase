import requests

class APIEntradas:

    def __init__(self, base_url="http://localhost:5000/api"):
        self.base_url = base_url
    def create(self,num_entrada):
        url= f"{self.base_url}/entradas/nueva/{num_entrada}"
        try:
            response = requests.get(url)
            return response.status_code,response.json()
        except:
            return 0, {"msg":"Se ha producido un error al conectar con el servidor"}