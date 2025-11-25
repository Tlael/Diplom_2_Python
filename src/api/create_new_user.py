import requests
import random
import string

from src.api.urls import create_user_url


# Генерация случайной строки из букв нижнего регистра
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choices(letters, k=length))
    return random_string


# Генерация случайного адреса электронной почты
def generate_email():
    local_part = generate_random_string(8)  # Часть до @
    domain = 'example.com'  # Доменное имя
    return f'{local_part}@{domain}'


# Регистрация нового пользователя
def register_new_user_and_return_response():
    # Генерация уникального логина, пароля и имени пользователя
    email = generate_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    # Формирование тела запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # Отправка запроса на регистрацию пользователя
    response = requests.post(create_user_url, json=payload)

    return response
