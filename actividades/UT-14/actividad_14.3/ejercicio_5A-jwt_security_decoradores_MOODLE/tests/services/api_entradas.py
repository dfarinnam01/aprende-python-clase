import requests

class APIEntradas:

    def __init__(self, token=None, base_url="http://127.0.0.1:5000/api/entradas"):
        self.base_url = base_url
        self.token = token

    # ############  INTERNA: CONFIGURA HEADER  ############
    def _headers(self):
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}

    # ############  CREATE  ############
    def create(self, data: dict):
        url = f"{self.base_url}"
        try:
            response = requests.post(
                url,
                json=data,
                headers=self._headers()
            )
            return response.status_code, response.json()
        except Exception as ex:
            return 0, {"message": "Se ha producido un error al conectar con el servidor"}

    # ############  LIST_ALL  ############
    def list_all(self):
        url = f"{self.base_url}"
        try:
            response = requests.get(
                url,
                headers=self._headers()
            )
            return response.status_code, response.json()
        except Exception:
            return 0, {"message": "Se ha producido un error al conectar con el servidor"}

    # ############  GET  ############
    def get(self, entrada_id: int):
        url = f"{self.base_url}/{entrada_id}"
        try:
            response = requests.get(
                url,
                headers=self._headers(),
            )
            return response.status_code, response.json()
        except Exception:
            return 0, {"message": "Se ha producido un error al conectar con el servidor"}

    # ############  DELETE  ############
    def delete(self, id: int):
        url = f"{self.base_url}/{id}"

        try:
            response = requests.delete(
                url,
                headers=self._headers()
            )
            return response.status_code, response.json()
        except Exception:
            return 0, {"message": "Error conexión"}

    # ############  UPDATE  ############
    def update(self, id:int, data: dict):
        url = f"{self.base_url}/{id}"

        try:
            response = requests.put(
                url,
                json=data,
                headers=self._headers()
            )
            return response.status_code, response.json()
        except Exception:
            return 0, {"message": "Error conexión"}