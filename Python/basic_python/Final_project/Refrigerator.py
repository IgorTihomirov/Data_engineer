import datetime
from decimal import Decimal

goods = {}
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



def add_by_note(items, note):
    parts = note.split() # разделяем строку на части
    last_part = [-1] # последняя часть строки
    pre_last_part = [-2] # предпоследняя часть строки
    if last_part == DATE_FORMAT: # Проверка последней части строки. Если она представляет дату в формате "год-месяц-день"
        expiration_date = datetime.datetime.strptime(last_part, DATE_FORMAT) #то она считается датой и сохраняется в переменную expiration_date
        amount = pre_last_part # предпоследняя часть строки считается количеством товара и сохраняется в переменную amount
        title = ' '.join(parts[:-2]) # все остальные части объединяются в название товара и сохраняются в переменную title
    else: #Проверка последней части строки. Если она не представляет датой
        amount = last_part # то она считается количеством товара и сохраняется в переменную amount
        title = ' '.join(parts[:-1])  # все остальные части объединяются в название товара и сохраняются в переменную title
        expiration_date = None # переменная expiration_date устанавливается в None
    add(items, title, amount, expiration_date=None) # Вызов функции add с извлеченными данными (название товара, количество, дата истечения) для добавления их в список items


add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
print(goods)
def find(items, needle):
    ...


def amount(items, needle):
    ...


def expire(items, in_advance_days=0):
    ...