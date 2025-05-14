import allure
from constants import *
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods

@allure.suite("Orders")
@allure.sub_suite("Принятие заказов")
class TestOrderAccept:

    @allure.title("Успешное принятие заказа")
    @allure.description("Проверка успешного принятия заказа курьером")
    def test_accept_order_success(self, create_courier):
        order_methods = OrderMethods()
        courier_methods = CourierMethods()
        _, create_order_response = order_methods.create_order(ORDER_DATASETS[0])
        order_id = order_methods.get_order_id_by_track(create_order_response["track"])
        courier_id = courier_methods.get_courier_id(create_courier["login"], create_courier["password"])
        status_code, response_json = order_methods.accept_order(order_id, courier_id)
        assert status_code == 200 and response_json == {'ok': True}

    @allure.title("Принятие заказа без курьера")
    @allure.description("Проверка ошибки при принятии заказа без указания курьера")
    def test_accept_order_without_courier_id_error(self):
        order_methods = OrderMethods()
        _, create_order_response = order_methods.create_order(ORDER_DATASETS[0])
        order_id = order_methods.get_order_id_by_track(create_order_response["track"])
        status_code, response_json = order_methods.accept_order(order_id, "")
        assert status_code == 400 and response_json == {
            'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title("Принятие заказа с неверным ID курьера")
    @allure.description("Проверка ошибки при принятии заказа с неверным ID курьера")
    def test_accept_order_with_non_exist_courier_id_error(self):
        order_methods = OrderMethods()
        _, create_order_response = order_methods.create_order(ORDER_DATASETS[0])
        order_id = order_methods.get_order_id_by_track(create_order_response["track"])
        status_code, response_json = order_methods.accept_order(order_id, "999999")
        assert status_code == 404 and response_json == {
            'code': 404, 'message': 'Курьера с таким id не существует'}

    @allure.title("Принятие заказа с неверным ID заказа")
    @allure.description("Проверка ошибки при принятии заказа с неверным ID заказа")
    def test_accept_order_non_exist_order_id_error(self, create_courier):
        order_methods = OrderMethods()
        courier_methods = CourierMethods()
        courier_id = courier_methods.get_courier_id(create_courier["login"], create_courier["password"])
        status_code, response_json = order_methods.accept_order("999999", courier_id)
        assert status_code == 404 and response_json == {
            'code': 404, 'message': 'Заказа с таким id не существует'}

    @allure.title("Принятие заказа без указания ID заказа")
    @allure.description("Проверка ошибки при принятии заказа без указания ID заказа")
    def test_accept_order_without_order_id_error(self, create_courier):
        order_methods = OrderMethods()
        courier_methods = CourierMethods()
        courier_id = courier_methods.get_courier_id(create_courier["login"], create_courier["password"])
        status_code, response_json = order_methods.accept_order("", courier_id)
        assert status_code == 404 and response_json == {'code': 404, 'message': 'Not Found.'}