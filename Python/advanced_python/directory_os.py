# Импортируйте библиотеку для создания директории для данных.
import os
import requests

cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': '',      # скорость ветра в "м/с"
        'T': ''       # передать символы в упрощённом виде
    }
    return params


def what_weather(city):
    url = make_url(city)
    weather_parameters = make_parameters()
    try:
        response = requests.get(url, params=weather_parameters)
        response.raise_for_status()
    except requests.ConnectionError:
        return '<ошибка на сервере погоды>'
    return response.text


# Напишите код для создания директории 'data' здесь.
os.makedirs("data", exist_ok=True) 

for city in cities:
    weather_report = what_weather(city)
    # Напишите код для сохранения файла с результатами 
    # запроса к сайту в текстовый файл в директории data,
    # в функции open используйте параметр encoding='utf-8'
    # для корректной записи символов.
    with open(f'data/{city}.txt', 'w', encoding='utf-8') as file:
        file.write(f'{weather_report}')