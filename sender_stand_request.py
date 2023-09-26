import configuration
import requests
import data

# функция для проверки открытия docs API
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# функция для возврата логов основного сервера
def get_logs():
        return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})

# функция для получения информации из БД
def get_users_table():
        return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# функция запроса на создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

# функция, которая получает на вход список id продуктов products_ids и возращает ответ с наборами
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
                         headers=data.headers)