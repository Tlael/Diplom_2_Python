import json

import allure
import requests

from resources.data_user import DATA
from resources.headers import HEADERS
from resources.message import email_or_pass_incorrect
from resources.urls import login_user_url


class TestLoginUser:
    @allure.title('Проверка логина пользователя')
    def test_login_user(self):
        data = DATA['test_login_user']
        data_string = json.dumps(data)
        response = requests.post(login_user_url, headers=HEADERS, data=data_string)
        assert 200 == response.status_code
        assert 'accessToken' in response.json()

    @allure.title('Проверка логина с неверным email')
    def test_login_user_incorrect_email(self):
        data = DATA['test_login_user_incorrect_email']
        data_string = json.dumps(data)
        response = requests.post(login_user_url, headers=HEADERS, data=data_string)

        assert 401 == response.status_code
        assert response.json()['message'] == email_or_pass_incorrect

    @allure.title('Проверка логина с неверным паролем')
    def test_login_user_incorrect_pass(self):
        data = DATA['test_login_user_incorrect_pass']
        data_string = json.dumps(data)
        response = requests.post(login_user_url, headers=HEADERS, data=data_string)
        assert 401 == response.status_code
        assert response.json()['message'] == email_or_pass_incorrect
