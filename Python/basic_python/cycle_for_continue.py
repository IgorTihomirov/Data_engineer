retailers = ['Pixi', 'Двоечка', 'Жёлтое и зелёное', 'Экология вкуса', 'Вкусняшка']
vegetables = ['Помидоры', 'Огурцы', 'Брюква', 'Баклажаны', 'Патиссоны']

for retailer in retailers:
    print(retailer)
    for vegetable in vegetables:
        # Если одновременно выполняются оба условия...
        if retailer == 'Жёлтое и зелёное' and vegetable == 'Брюква':
            # ...не выполняем текущую итерацию, а сразу переходим к следующей.
            continue
        print(f'- {vegetable} для сети «{retailer}»')

print('Погрузка завершена.')