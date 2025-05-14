import requests
from constants import *

class OrderMethods:

    def create_order(self, order_data):
        payload = order_data
        response = requests.post(ORDERS_URL, json=payload)
        return response.status_code, response.json()

    def get_orders(self):
        response = requests.get(ORDERS_URL)
        return response.status_code, response.json()

    def get_order_by_track(self, track):
        params = {"t": track}
        response = requests.get(ORDERS_TRACK_URL, params=params)
        return response.status_code, response.json()

    def get_order_id_by_track(self, track):
        status_code, response_json = self.get_order_by_track(track)
        if status_code == 200:
            order_id = response_json["order"]["id"]
            return order_id
        else:
            return None

    def accept_order(self, order_id, courier_id):
        params = { "courierId": courier_id }
        response = requests.put(f"{ORDERS_ACCEPT_URL}/{order_id}", params=params)
        return response.status_code, response.json()

