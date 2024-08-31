import requests

from data import ScooterApiData
import allure

from scooter_api import CourierApi as courier_api
from helper import login_and_delete, modify_courier_data, delete_data_field


class TestCreateCourier:
    @allure.title('Проверяем создание курьера')
    def test_successful_create_courier(self, generate_registration_data):
        courier_data = generate_registration_data
        response = courier_api.create(courier_data)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        assert login_and_delete(courier_data).status_code == 200

    @allure.title('Проверяем успешный код ответа при создании курьера')
    def test_create_one_courier_success_response_code(self, generate_registration_data):
        courier_data = generate_registration_data
        response = courier_api.create(courier_data)
        assert response.text == '{"ok":true}'
        assert login_and_delete(courier_data).status_code == 200

    @allure.title('Проверка на создание двух курьеров с одинаковыми данными')
    def test_create_two_similar_couriers(self, generate_registration_data):
        courier_data = generate_registration_data
        courier_api.create(courier_data)
        response = courier_api.create(courier_data)
        assert response.status_code == 409
        assert response.text == '{"message": "Этот логин уже используется"}'
        assert login_and_delete(courier_data).status_code == 200

    @allure.title('Проверка создания двух курьеров с одинаковыми логинами и разными паролями')
    def test_create_two_similar_couriers_with_different_passwords(self, generate_registration_data):
        courier_data = generate_registration_data
        courier_api.create(courier_data)
        modified_data = modify_courier_data(courier_data, 'password', '12345a')
        response2 = courier_api.create(modified_data)
        assert response2.status_code == 409
        assert response2.text == '{"message": "Этот логин уже используется"}'
        assert login_and_delete(courier_data).status_code == 200

    @allure.title('Проверка на создание курьера без указания пароля')
    def test_create_courier_without_password(self, generate_registration_data):
        courier_data = generate_registration_data
        delete_data_field(courier_data,'password')
        response = requests.post(ScooterApiData.CREATE_COURIER_POST_URL, generate_registration_data)
        assert response.status_code == 400
        assert response.text == '{"message": "Недостаточно данных для создания учетной записи"}'
