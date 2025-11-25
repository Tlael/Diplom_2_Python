import json
from copy import deepcopy

import requests

from resources.headers import HEADERS
from resources.urls import get_user_url


def save_and_restore(authenticated_user, field_to_update, new_value):
    # Получение текущих данных
    response = requests.get(get_user_url, headers={'Authorization': authenticated_user})
    current_data = response.json()

    # Обновление данных
    patch_data = {field_to_update: new_value}
    patch_data_string = json.dumps(patch_data)

    # Подготовка заголовков с токеном
    update_headers = deepcopy(HEADERS)
    update_headers['Authorization'] = authenticated_user

    # Обновление данных
    update_response = requests.patch(get_user_url, headers=update_headers, data=patch_data_string)
    assert 200 == update_response.status_code

    # Проверка успешного обновления
    updated_field = update_response.json()['user'].get(field_to_update)
    assert updated_field == new_value

    # Восстановление исходных данных
    restore_data = {field_to_update: current_data['user'][field_to_update]}
    restore_data_string = json.dumps(restore_data)

    # Отправка запроса на восстановление
    restore_response = requests.patch(get_user_url, headers=update_headers, data=restore_data_string)
    assert 200 == restore_response.status_code

    # Проверка успешного восстановления
    restored_field = restore_response.json()['user'].get(field_to_update)
    assert restored_field == current_data['user'][field_to_update]
