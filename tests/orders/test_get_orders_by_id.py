import allure
from methods.order_methods import OrderMethods

@allure.suite("Orders")
@allure.sub_suite("Получение списка заказов по ID")
class TestGetOrdersById:

    @allure.title("Получение существующего заказа по номеру")
    @allure.description("Проверка успешного получения существующего заказа по номеру")
    def test_get_order_by_id_success(self, create_order):
        order_methods = OrderMethods()
        track_id = create_order["track"]
        status_code, response_json = order_methods.get_order_by_track(track_id)
        assert status_code == 200 and "order" in response_json

    @allure.title("Получение заказа с пустым номером")
    @allure.description("Проверка ошибки при запросе заказа с пустым полем номера в запросе")
    def test_get_order_by_id_without_id_error(self):
        order_methods = OrderMethods()
        status_code, response_json = order_methods.get_order_by_track("")
        assert status_code == 400 and response_json == {
            'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title("Получение заказа по несуществующему номеру")
    @allure.description("Проверка ошибки при запросе заказа по несуществующему номеру")
    def test_get_order_by_id_non_exist_id_error(self):
        order_methods = OrderMethods()
        status_code, response_json = order_methods.get_order_by_track("999999")
        assert status_code == 404 and response_json == {
            'code': 404, 'message': 'Заказ не найден'}