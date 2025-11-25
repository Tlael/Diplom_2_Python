import json
import allure
import requests

from src.data.change_data_user import save_and_restore
from src.data.data_user import DATA
from src.data.message import not_auth

from src.api.headers import HEADERS
from src.api.urls import get_user_url


class TestChangeUserData:
    @allure.title('Проверка изменения email пользователя с авторизацией')
    def test_change_email_with_auth(self, authenticated_user):
        save_and_restore(
            authenticated_user=authenticated_user,
            field_to_update='email',
            new_value=DATA['test_patch_user_email']['email']
        )

    @allure.title('Проверка изменения name пользователя с авторизацией')
    def test_change_name_with_auth(self, authenticated_user):
        save_and_restore(
            authenticated_user=authenticated_user,
            field_to_update='name',
            new_value=DATA['test_patch_user_name']['name']
        )

    @allure.title('Проверка попытки изменения email без авторизации')
    def test_change_email_without_auth(self):
        # Определяем новое значение email
        new_email = DATA['test_patch_user_email']['email']

        # Формируем данные для PATCH-запроса
        patch_data = {'email': new_email}
        patch_data_string = json.dumps(patch_data)

        # Отправляем запрос без авторизационных заголовков
        unauthorized_response = requests.patch(get_user_url, headers=HEADERS, data=patch_data_string)

        # Проверяем, что сервер вернул ошибку авторизации
        assert unauthorized_response.status_code == 401
        assert unauthorized_response.json()["message"] == not_auth

    @allure.title('Проверка попытки изменения name без авторизации')
    def test_change_name_without_auth(self):
        # Определяем новое значение имени
        new_name = DATA['test_patch_user_name']['name']

        # Формируем данные для PATCH-запроса
        patch_data = {'name': new_name}
        patch_data_string = json.dumps(patch_data)

        # Отправляем запрос без авторизационных заголовков
        unauthorized_response = requests.patch(get_user_url, headers=HEADERS, data=patch_data_string)

        # Проверяем, что сервер вернул ошибку авторизации
        assert unauthorized_response.status_code == 401
        assert unauthorized_response.json()["message"] == not_auth
