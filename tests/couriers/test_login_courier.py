import allure
import pytest
from constants import *
from methods.courier_methods import CourierMethods

@allure.suite("Courier")
@allure.sub_suite("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка успешной авторизации курьера")
    def test_courier_login_success(self, create_courier):
        courier_methods = CourierMethods()
        login = create_courier["login"]
        password = create_courier["password"]
        status_code, response_json = courier_methods.login_courier(login, password)
        assert status_code == 200 and "id" in response_json

    @allure.title("Авторизация с неверным логином")
    @allure.description("Проверка ошибки при авторизации курьера с неверным логином")
    def test_courier_login_with_wrong_login_error(self, create_courier):
        courier_methods = CourierMethods()
        login = WRONG_COURIER_DATA["login"]
        password = create_courier["password"]
        status_code, response_json = courier_methods.login_courier(login, password)
        assert status_code == 404 and response_json == {
            'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверка ошибки при авторизации курьера с неверным паролем")
    def test_courier_login_with_wrong_password_error(self, create_courier):
        courier_methods = CourierMethods()
        login = create_courier["login"]
        password = WRONG_COURIER_DATA["password"]
        status_code, response_json = courier_methods.login_courier(login, password)
        assert status_code == 404 and response_json == {
            'code': 404, 'message': 'Учетная запись не найдена'}

    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_courier_login_with_empty_field_error(self, create_courier, empty_field):
        allure.dynamic.title(f"Авторизация без поля {empty_field}")
        allure.dynamic.description(f"Проверка ошибки при авторизации курьера без заполнения поля {empty_field}")
        courier_methods = CourierMethods()
        courier_data = create_courier
        courier_data[empty_field] = ""
        login = create_courier["login"]
        password = create_courier["password"]
        status_code, response_json = courier_methods.login_courier(login, password)
        assert status_code == 400 and response_json == {
            'code': 400, 'message': 'Недостаточно данных для входа'}