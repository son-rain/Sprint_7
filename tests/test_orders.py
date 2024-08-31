import json

import allure
import pytest

from data import OrderData
from scooter_api import OrdersApi as order_api


class TestOrders:
    @pytest.mark.parametrize("order_data", OrderData.payload)
    @allure.title("Проверка успешного оформления заказа с разными комбинациями цвета самоката")
    def test_create_order_with_different_colours(self, order_data):
        response = order_api.create_order(order_data)
        assert 'track' in response.text

    @allure.title("Проверка получения списка заказов")
    def test_successful_get_orders_list(self):
        response = order_api.get_order_list()
        assert response.status_code == 200








