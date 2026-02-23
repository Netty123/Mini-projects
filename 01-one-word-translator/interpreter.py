# Переводчик слова(с русского на английский)

import requests
from pprint import pprint

api_key = 'АПИ ключ от яндекс переводчика'
url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=API-ключ&lang=en-ru&text=time'

translation = input('Введите слово на русском языке: ')

# Переменная params содержит параметры для APi-запроса
params = {
    'key': api_key,
    'lang': 'ru-en', 
    'text': translation
}

respons = requests.get(url, params=params) # отправляем get-запрос
print(respons.json()['def'][0]['tr'][0]['text'])