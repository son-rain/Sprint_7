import json

import allure
import requests

from data import ScooterApiData


class CourierApi:

    @staticmethod
    @allure.step("Создаём нового курьера")
    def create(register_user_payload):
        reg_response = requests.post(ScooterApiData.CREATE_COURIER_POST_URL, register_user_payload)
        return reg_response

    @staticmethod
    @allure.step("Отправляем запрос на логин курьера")
    def login(courier_data):
        login_response = requests.post(ScooterApiData.LOGIN_COURIER_POST_URL, courier_data)
        return login_response

    @staticmethod
    @allure.step("Удаляем курьера по id")
    def delete(courier_id):
        del_response = requests.delete(f'{ScooterApiData.DELETE_COURIER_URL}/{courier_id}')
        return del_response


class OrdersApi:
    @staticmethod
    @allure.step("Отправляем запрос на создание нового заказа")
    def create_order(order_data):
        response = requests.post(ScooterApiData.CREATE_ORDER_POST_URL, json.dumps(order_data))
        return response

    @staticmethod
    @allure.step("Отправляем запрос на получение списка заказов")
    def get_order_list():
        order_list_response = requests.get(f'{ScooterApiData.GET_ORDERS_LIST_URL}')
        return order_list_response






