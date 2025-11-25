import allure
import requests

from src.data.message import not_auth

from src.api.urls import get_order_user_url


class TestOrders:
    @allure.title('Проверка получения заказов авторизированным пользователем')
    def test_get_orders_with_auth(self, authenticated_user):
        headers = {
            'Authorization': f'{authenticated_user}'
        }
        orders_response = requests.get(get_order_user_url, headers=headers)

        assert 200 == orders_response.status_code
        assert 'orders' in orders_response.json()

    @allure.title('Проверка получения заказов не авторизированным пользователем')
    def test_get_orders_not_auth(self):
        response = requests.get(get_order_user_url)

        assert 401 == response.status_code
        assert response.json()["message"] == not_auth
