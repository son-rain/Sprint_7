import requests


class ScooterApiData:
    SCOOTER_MAIN_URL = "https://qa-scooter.praktikum-services.ru"
    CREATE_COURIER_POST_URL = f'{SCOOTER_MAIN_URL}/api/v1/courier'
    DELETE_COURIER_URL = f'{SCOOTER_MAIN_URL}/api/v1/courier/'
    LOGIN_COURIER_POST_URL = f'{SCOOTER_MAIN_URL}/api/v1/courier/login'
    CREATE_ORDER_POST_URL = f'{SCOOTER_MAIN_URL}/api/v1/orders'
    ACCEPT_ORDER_PUT_URL = f'{SCOOTER_MAIN_URL}/api/v1/orders/accept/'
    GET_ORDERS_LIST_URL = f'{SCOOTER_MAIN_URL}/api/v1/orders'
    CANCEL_ORDER_PUT_URL = f'{SCOOTER_MAIN_URL}/api/v1/orders/cancel'

    LOGIN_DATA = {
        "login": 'courier_1',
        "password": '123456'
    }

    REGISTRATION_DATA = {
        "login": 'courier_1',
        "password": '123456'
    }


class OrderData:
    payload = [{
        "firstName": "Густав",
        "lastName": "Нарышкин",
        "address": "Маросейко, 24",
        "metroStation": 5,
        "phone": "+7 980 354 00 00",
        "rentTime": 4,
        "deliveryDate": "2024-07-11",
        "comment": "Лучше привезите",
        "color": ["BLACK"]
    },
        {
            "firstName": "Ярослав",
            "lastName": "Гудейко",
            "address": "Багамы, 19",
            "metroStation": 1,
            "phone": "+7 800 900 45 45",
            "rentTime": 1,
            "deliveryDate": "2025-09-09",
            "comment": "Жеесть",
            "color": ["BLACK", "GRAY"]
        },
        {
            "firstName": "Гудослав",
            "lastName": "Пошейко",
            "address": "Панама, 139",
            "metroStation": 15,
            "phone": "+7 967 111 11 09",
            "rentTime": 3,
            "deliveryDate": "2019-07-09",
            "comment": "Жеесть2",
            "color": []
        }
    ]



