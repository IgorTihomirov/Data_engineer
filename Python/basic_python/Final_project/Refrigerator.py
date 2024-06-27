import datetime as dt
from decimal import Decimal

goods = {
    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},
        {'amount': Decimal('1'), 'expiration_date': dt.date(2023, 12, 9)}
    ],
    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': dt.date(2023, 12, 12)},
        {'amount': Decimal('3'), 'expiration_date': dt.date(2023, 12, 11)}
    ],
    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(
        expiration_date,
        DATE_FORMAT
    ).date() if expiration_date else expiration_date
    list.append(
        items[title],
{'amount': amount, 'expiration_date': expiration_date}
    )


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
        if needle.lower() in title.lower():
            result.append(title)
    return result


#print(find(goods, 'йц'))


def amount(items, needle):
    product_amount = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            product_amount += part['amount']
    return product_amount


#print(amount(goods, 'яйца'))
# Вывод: 1
#print(amount(goods, 'хЛЕб'))
# Вывод: 5

def expire(items, in_advance_days=0):
    result = []
    today = dt.date.today()
    for title, parts in items.items():
        amount = Decimal('0')
        for i in parts:
            expiration_date = i.get('expiration_date')
            if expiration_date and expiration_date <= today + dt.timedelta(days=in_advance_days):
                amount += i.get('amount')
        if amount > 0:
            result.append((title, amount))
    return result

print(expire(goods))
# Вывод: [('Хлеб', Decimal('1'))]
print(expire(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
print(expire(goods, 2))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]