retailers = ['Pixi', 'Двоечка', 'Жёлтое и зелёное', 'Экология вкуса', 'Вкусняшка']
vegetables = ['Помидоры', 'Огурцы', 'Брюква', 'Баклажаны', 'Патиссоны']

for retailer in retailers:
    if retailer == 'Экология вкуса':
        break
    print(retailer)
    for vegetable in vegetables:
        if retailer == 'Жёлтое и зелёное' and vegetable == 'Брюква':
            continue
        # Если одновременно выполнились эти условия...
        if retailer == 'Двоечка' and vegetable == 'Огурцы':
            # ...прерываем этот (вложенный) цикл:
            break
        print(f'- {vegetable} для сети «{retailer}»')

print('Погрузка завершена.')