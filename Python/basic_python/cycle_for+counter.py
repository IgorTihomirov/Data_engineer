def count_canisters(temperatures_per_day):
    hot_days_counter = 0
    #hot_days_conter = [for day in temperatures_per_day]
    for i in temperatures_per_day:
        if i >= 30:
            hot_days_counter += 1
    return hot_days_counter


forecast_temperatures = [26, 28, 30, 31, 29, 31, 28, 26]
# Вызовите функцию и напечатайте результат в нужном формате.

print(f'Нужно канистр: {count_canisters(forecast_temperatures)}')
