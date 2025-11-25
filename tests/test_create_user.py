import json

import allure
import requests

from src.data.data_user import DATA
from src.data.message import user_already_exists, not_enough_data

from src.api.headers import HEADERS
from src.api.urls import create_user_url
from src.api.create_new_user import register_new_user_and_return_response


class TestCreateUser:
    @allure.title('Проверка регистрации уникального пользователя')
    def test_create_user(self):
        response = register_new_user_and_return_response()

        assert 200 == response.status_code
        assert 'accessToken' in response.json()

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_create_user_re_registration(self):
        data = DATA["test_create_user_re_registration"]
        data_string = json.dumps(data)
        response = requests.post(create_user_url, headers=HEADERS, data=data_string)

        assert 403 == response.status_code
        assert response.json()['message'] == user_already_exists

    @allure.title('Проверка создания пользователя без email')
    def test_create_user_without_email(self):
        data = DATA["test_create_user_without_email"]
        data_string = json.dumps(data)
        response = requests.post(create_user_url, headers=HEADERS, data=data_string)

        assert 403 == response.status_code
        assert response.json()['message'] == not_enough_data

    @allure.title('Проверка создания пользователя без пароля')
    def test_create_user_without_email(self):
        data = DATA["test_create_user_without_pass"]
        data_string = json.dumps(data)
        response = requests.post(create_user_url, headers=HEADERS, data=data_string)

        assert 403 == response.status_code
        assert response.json()['message'] == not_enough_data
