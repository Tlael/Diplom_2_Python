import json

import allure
import requests

from resources.data_order import DATA_ORDER
from resources.headers import HEADERS
from resources.message import no_ingredients
from resources.urls import create_order_url


class TestCreateOrders:
    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_auth(self, authenticated_user):
        data = DATA_ORDER['test_create_order_with_ingredients']
        data_string = json.dumps(data)
        response = requests.post(create_order_url, headers=HEADERS, data=data_string)

        assert 200 == response.status_code
        assert 'order' in response.json()

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_auth(self):
        data = DATA_ORDER['test_create_order_with_ingredients']
        data_string = json.dumps(data)
        response = requests.post(create_order_url, headers=HEADERS, data=data_string)

        assert 200 == response.status_code
        assert 'order' in response.json()

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        data = DATA_ORDER['test_create_order_without_ingredients']
        data_string = json.dumps(data)
        response = requests.post(create_order_url, headers=HEADERS, data=data_string)

        assert 400 == response.status_code
        assert response.json()['message'] == no_ingredients

    @allure.title('Проверка создания заказа с неверным хэшом ингредиентов')
    def test_create_order_without_ingredients(self):
        data = DATA_ORDER['test_create_order_invalid_hash']
        data_string = json.dumps(data)
        response = requests.post(create_order_url, headers=HEADERS, data=data_string)

        assert 500 == response.status_code
