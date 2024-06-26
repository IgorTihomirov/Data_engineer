import datetime
from decimal import Decimal

goods = {}
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = datetime.datetime.strptime(
        expiration_date,
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items, note):
    parts = str.split(note, ' ')
    if len(str.split(parts[-1], '-')) == 3:
        add(items, ' '.join(parts[:-2]), Decimal(parts[-2]), parts[-1])
    else:
        add(items, ' '.join(parts[:-1]), Decimal(parts[-1]))


add_by_note({}, 'Яйца гусиные 4 2023-07-15')
add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15')
print(goods)


def find(items, needle):
    ...


def amount(items, needle):
    ...


def expire(items, in_advance_days=0):
    ...