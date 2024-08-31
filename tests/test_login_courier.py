import allure
import requests
from data import ScooterApiData
from scooter_api import CourierApi as courier_api
from helper import modify_courier_data


class TestLoginCourier:
    @allure.title("Проверка авторизации курьера с валидными данными")
    def test_login_courier(self):
        courier_api.create(ScooterApiData.REGISTRATION_DATA)
        response = courier_api.login(ScooterApiData.LOGIN_DATA)
        assert 'id' in response.text
        assert courier_api.delete(ScooterApiData.LOGIN_DATA).status_code == 200

    @allure.title("Проверка авторизации курьера без пароля")
    def test_login_courier_without_password(self):
        login_data = ScooterApiData.LOGIN_DATA
        modified_data = modify_courier_data(login_data, 'password', '')
        response = requests.post(ScooterApiData.LOGIN_COURIER_POST_URL, modified_data)
        assert response.text == {"message":  "Недостаточно данных для входа"}

    @allure.title("Проверка авторизации курьера с неверным логином")
    def test_login_courier_with_incorrect_login(self):
        login_data = ScooterApiData.LOGIN_DATA
        modified_data = modify_courier_data(login_data, 'login', 'user123')
        response = requests.post(ScooterApiData.LOGIN_COURIER_POST_URL, modified_data)
        assert response.text == {"message":  "Учетная запись не найдена"}
