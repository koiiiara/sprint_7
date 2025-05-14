import requests
from constants import *

class CourierMethods:

    def create_courier(self, login, password, first_name):
        payload = {}
        if login:
            payload["login"] = login
        if password:
            payload["password"] = password
        if first_name:
            payload["firstName"] = first_name

        response = requests.post(COURIER_URL, data=payload)
        return response.status_code, response.json()

    def delete_courier(self, user_id):
        response = requests.delete(f"{COURIER_URL}/{user_id}")
        return response.status_code, response.json()

    def get_courier_id(self, login, password):
        status_code, response_json = self.login_courier(login, password)
        if status_code == 200:
            return response_json["id"]
        else:
            return None

    def login_courier(self, login, password):
        json_data = {
            "login": login,
            "password": password
        }
        response = requests.post(LOGIN_COURIER_URL, json=json_data)
        return response.status_code, response.json()



