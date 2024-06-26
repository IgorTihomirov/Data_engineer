import datetime
from decimal import Decimal

goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 6, 24)}],
    'Яйца гусиные': [{'amount': Decimal('4'), 'expiration_date': datetime.date(2023, 7, 15)}],
    'Морковь': [{'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 6)}]
}
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

#print(goods)


def find(items, needle):
    result = []
    for title in items:
        if needle in str.lower(title):
            result = list.append(result, needle)
            return result


print(find(goods, 'йц'))


def amount(items, needle):
    ...


def expire(items, in_advance_days=0):
    ...