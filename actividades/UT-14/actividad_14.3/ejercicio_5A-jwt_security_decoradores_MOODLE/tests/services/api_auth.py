import requests

class APIAuth:

    def __init__(self):
        self.base_url = "http://localhost:5000/api/auth"
        self.token = None

    # ############  REGISTER  ############
    def register(self, username, password):
        response = requests.post(f"{self.base_url}/register", json={
            "username": username,
            "password": password
        })
        return response.status_code, response.json()

    # ############  LOGIN  ############
    def login(self, username:str, password:str):
        response = requests.post(f"{self.base_url}/login", json={
            "username": username,
            "password": password
        })

        if response.status_code == 200:
            self.token = response.json()["access_token"]
            return response.status_code, self.token

        return 0, {"message": "Error de conexión login"}

    # ############  LOGIN  ############
    def users(self):
        return self._get(f"{self.base_url}/users")


    # ========================================
    # ===  ENDPOINTS SOLO  PARA DESARROLLO
    # ========================================

    # ############  REGISTER  ############
    def register_developer(self, username, password, role):
        response = requests.post(f"{self.base_url}/register-developer", json={
            "username": username,
            "password": password,
            "role": role
        })
        data = response.json()
        return response.status_code, response.json()


    # ############  CONSULTA COMPLETA DEL TOKEN  ############
    def token_full_info(self):
        url = f"{self.base_url}/token/full-info"
        return self._get(url)

    # ############  CONSULTA SIMPLE DEL TOKEN  ############
    def token_simple_info(self):
        url = f"{self.base_url}/token/simple-info"
        return self._get(url)


    # =========================
    # PETICIONES CON TOKEN
    # =========================
    def _get(self, url):
        headers = self._headers()

        try:
            response = requests.get(url, headers=headers)
            return response.status_code, response.json()
        except Exception:
            return 0, {"message": "Error conexión"}

    def _headers(self):
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}