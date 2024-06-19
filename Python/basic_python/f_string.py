# Количество корзин с овощами, шт.
baskets = 462
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(baskets, average_weight, price_per_kg):
    total_weight = baskets * average_weight
    total_price = total_weight * price_per_kg
    return total_weight, total_price

# Вызовите функцию calc() и обработайте вернувшееся значение.
a, b = calc(462, 25, 175)

# Составьте f-строку и напечатайте её.
print(f'Общий вес урожая: {a} кг. Оценённая стоимость урожая: {b}.')