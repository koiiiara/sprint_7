import allure
import pytest
from constants import *
from methods.order_methods import OrderMethods

@allure.suite("Orders")
@allure.sub_suite("Создание заказа")
class TestCreateOrders:

    @pytest.mark.parametrize("order_data", ORDER_DATASETS)
    def test_create_order_with_different_colors(self, order_data):
        allure.dynamic.title(f"Создание заказа с полем color=\"{order_data['color']}\"")
        allure.dynamic.description(f"Проверка успешного создание заказа с полем color=\"{order_data['color']}\"")
        order_methods = OrderMethods()
        status_code, response_json = order_methods.create_order(order_data)
        assert status_code == 201 and "track" in response_json