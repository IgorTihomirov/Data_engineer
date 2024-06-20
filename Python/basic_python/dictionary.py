#Напишите функцию create_vegetable_info(),
# которая вернёт словарь, где ключами будут названия овощей,
# а значениями — кортежи, первый элемент которых — сорт овоща, а второй — его урожайность.

# Функция для создания словаря информации об овощах

def create_vegetable_info(vegetables, varieties, yields):
    zip_collection = zip(varieties, yields)
    zip_collection1 = zip(vegetables, zip_collection)
    vegetable_info = dict(zip_collection1)
    return vegetable_info

# Тестовые данные:
vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]

# Вызов функции:
print(create_vegetable_info(vegetables, varieties, yields))