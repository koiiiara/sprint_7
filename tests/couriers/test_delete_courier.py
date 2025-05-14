import allure
from methods.courier_methods import CourierMethods

@allure.suite("Courier")
@allure.sub_suite("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Успешное удаление")
    @allure.description("Проверка успешного удаления курьера")
    def test_delete_courier_success(self, create_courier):
        courier_methods = CourierMethods()
        login = create_courier["login"]
        password = create_courier["password"]
        courier_id = courier_methods.get_courier_id(login, password)
        status_code, response_json = courier_methods.delete_courier(courier_id)
        assert status_code == 200 and response_json == {"ok": True}

    @allure.title("Удаление несуществующего курьера")
    @allure.description("Проверка ошибки при попытке удаления несуществующего курьера")
    def test_delete_courier_non_exist_id_error(self):
        courier_methods = CourierMethods()
        status_code, response_json = courier_methods.delete_courier("999999")
        assert status_code == 404 and response_json == {'code': 404, 'message': 'Курьера с таким id нет.'}


    @allure.title("Удаление курьера без указания ID")
    @allure.description("Проверка ошибки при попытке удаления курьера без указания ID")
    def test_delete_courier_without_id_error(self):
        courier_methods = CourierMethods()
        status_code, response_json = courier_methods.delete_courier("")
        assert status_code == 404 and response_json == {'code': 404, 'message': 'Not Found.'}

