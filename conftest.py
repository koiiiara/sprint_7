import pytest
from user_generator import generate_courier
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods

from constants import *

@pytest.fixture
def generate_user_for_create():
    user_data = generate_courier()
    yield user_data
    courier_methods = CourierMethods()
    user_id = courier_methods.get_courier_id(user_data["login"], user_data["password"])
    if user_id:
        courier_methods.delete_courier(user_id)

@pytest.fixture
def create_courier(generate_user_for_create):
    courier_methods = CourierMethods()
    login = generate_user_for_create["login"]
    password = generate_user_for_create["password"]
    first_name = generate_user_for_create["first_name"]
    status_code, response_json = courier_methods.create_courier(login, password, first_name)
    if status_code == 201:
        yield generate_user_for_create
    else:
        raise RuntimeError(
            f"Не удалось создать курьера: {status_code}, {response_json}"
        )

@pytest.fixture
def create_order():
    order_methods = OrderMethods()
    order_data = ORDER_DATASETS[0]
    status_code, response_json = order_methods.create_order(order_data)

    if status_code == 201 and "track" in response_json:
        yield response_json
    else:
        raise RuntimeError(
            f"Не удалось создать заказ: {status_code}, {response_json}"
        )




