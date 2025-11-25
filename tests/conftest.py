import pytest
import json
import requests

from src.data.data_user import DATA

from src.api.headers import HEADERS
from src.api.urls import login_user_url

@pytest.fixture
def authenticated_user(scope="session"):
    "Фикстура для получения токена авторизованного пользователя"
    login_data = DATA['test_login_user']
    login_data_string = json.dumps(login_data)
    login_response = requests.post(login_user_url, headers=HEADERS, data=login_data_string)
    access_token = login_response.json().get('accessToken')
    return access_token
