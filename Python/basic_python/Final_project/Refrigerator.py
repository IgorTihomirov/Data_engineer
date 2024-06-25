import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)}
    ],
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}]
}
DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    if expiration_date == None:  # Если expiration_date не предоставлено (равно None), оставить expiration_date без изменений.
        if title not in items: # Если название товара не существует как ключ в словаре items
            items[title] = []  # то создать пустой список для этого товара.
        items[title].append({'amount': amount, 'expiration_date': None}) # Добавить в список items[title] словарь, содержащий информацию о количестве товара good_amount и дате истечения expiration_date, если он был предоставлен
    else :
        date = datetime.datetime.strptime(expiration_date, DATE_FORMAT)  # Первый datetime это модуль, второй datetime - это класс в модуля datetime
        if title not in items: # Если название товара не существует как ключ в словаре items
            items[title] = []  # то создать пустой список для этого товара.
        items[title].append({'amount': amount, 'expiration_date': date.date()}) #Добавить в список items[title] словарь, содержащий информацию о количестве товара good_amount и дате истечения expiration_date, если он был предоставлен

add(goods, 'Яйца', Decimal('10'), '2023-9-30')
print(goods)


def add_by_note(items, note):
    ...


def find(items, needle):
    ...


def amount(items, needle):
    ...


def expire(items, in_advance_days=0):
    ...