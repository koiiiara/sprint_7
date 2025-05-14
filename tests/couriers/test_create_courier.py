import copy
import pytest
import allure
from methods.courier_methods import CourierMethods

@allure.suite("Courier")
@allure.sub_suite("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Проверка успешного создания курьера с валидными данными")
    def test_create_courier_success(self, generate_user_for_create):
        courier_methods = CourierMethods()
        login = generate_user_for_create["login"]
        password = generate_user_for_create["password"]
        first_name = generate_user_for_create["first_name"]
        status_code, response_json = courier_methods.create_courier(login, password, first_name)
        assert status_code == 201 and response_json == {"ok": True}

    @allure.title("Создание курьера без имени")
    @allure.description("Проверка успешного создания курьера без указания имени")
    def test_create_courier_without_name_error(self, generate_user_for_create):
        courier_methods = CourierMethods()
        login = generate_user_for_create["login"]
        password = generate_user_for_create["password"]
        status_code, response_json = courier_methods.create_courier(login, password, "")
        assert status_code == 201 and response_json == {"ok": True}

    @allure.title("Создание дубликата курьера")
    @allure.description("Проверка ошибки при создании курьера с уже существующими реквизитами")
    def test_create_courier_duplicate_error(self, create_courier):
        courier_methods = CourierMethods()
        login = create_courier["login"]
        password = create_courier["password"]
        first_name = create_courier["first_name"]
        status_code, response_json = courier_methods.create_courier(login, password, first_name)
        assert status_code == 409 and response_json == {
            "code":409,"message":"Этот логин уже используется. Попробуйте другой."}


    @allure.title("Создание курьера без логина")
    @allure.description("Проверка ошибки при создании курьера без указания логина")
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_create_courier_without_login_error(self, generate_user_for_create, empty_field):
        allure.dynamic.title(f"Создание курьера без поля {empty_field}")
        allure.dynamic.description(f"Проверка ошибки при создании курьера без заполнения поля {empty_field}")
        courier_methods = CourierMethods()
        user_data = copy.deepcopy(generate_user_for_create)
        user_data[empty_field] = None
        status_code, response_json = courier_methods.create_courier(user_data["login"],
                                                                    user_data["password"],
                                                                    user_data["first_name"])
        assert status_code == 400 and response_json == {
            "code":400,"message":"Недостаточно данных для создания учетной записи"}