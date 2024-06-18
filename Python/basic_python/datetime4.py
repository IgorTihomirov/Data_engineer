# Пропишите нужные импорты.
from decimal import Decimal, getcontext


# Напишите код функции.
def get_monthly_payment(sum_credit, number_of_months, percent):
    # Банк делит названную сумму на названное количество месяцев
    # и увеличивает ежемесячный платёж на оговоренный процент.
    getcontext().prec = 3
    amount_of_payment = (Decimal(sum_credit) / Decimal(number_of_months)) + (Decimal(sum_credit) / Decimal(number_of_months) * Decimal(percent)) / 100
    # Функция должна вернуть сумму ежемесячного платежа по кредиту.
    return amount_of_payment

# Вызовите функцию get_monthly_payment()
# с указанными в задании аргументами
# и распечатайте нужное сообщение.
payment = get_monthly_payment(54, 24, 9)
print('Ежемесячный платёж:', payment, 'ВтК')