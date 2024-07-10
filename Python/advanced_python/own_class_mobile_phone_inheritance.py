class Phone:
    # Тип телефона
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    # Переопределить значение атрибута line_type класса Phone.
    line_type = 'беспроводной'
    # Тип батареи
    battery_type = 'Li-ion'

    # Инициализатор класса MobilePhone с новым параметром:
    # network_type(Стандарт беспроводной связи)
    def __init__(self, dial_type_value, network_type):
        # Новый атрибут объекта
        self.network_type = network_type
        # Вызов родительского инициализатора
        super().__init__(dial_type_value)
        
    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-дзынь!')

    # Новый метод - запуск игры
    def start_game(self):
        print('Игра запущена!')


mobile_phone = MobilePhone('сенсорный', 'LTE')

print(mobile_phone.battery_type)
print(mobile_phone.network_type)
mobile_phone.start_game()

# Вывод:
# Li-ion
# LTE
# Игра запущена! 