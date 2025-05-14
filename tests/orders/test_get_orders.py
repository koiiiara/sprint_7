import allure
from methods.order_methods import OrderMethods

@allure.suite("Orders")
@allure.sub_suite("Получение списка заказов")
class TestGetOrders:

    @allure.title("Запрос списка всех заказов")
    @allure.description("Проверка успешного получения списка всех заказов")
    def test_get_orders_success(self):
        order_methods = OrderMethods()
        status_code, response_json = order_methods.get_orders()
        assert "orders" in response_json and isinstance(response_json["orders"], list)
