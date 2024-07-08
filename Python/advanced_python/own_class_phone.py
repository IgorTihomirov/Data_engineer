class Phone:
    # Атрибут класса.
    line_type = 'проводной'

    # Это инициализатор/конструктор класса, в котором объявлено два параметра.
    def __init__(self, dial_type_value):
        # Вот он - атрибут объекта. dial_type - атрибут объекта
        # dial_type_value - значение для атрибута объекта,
        # которое берется из параметра конструктора.
        self.dial_type = dial_type_value


# Создать объект rotary_phone со значением dial_type_value,
# равным 'дисковый'.
rotary_phone = Phone(dial_type_value='дисковый')
# Создать объект keypad_phone со значением dial_type_value,
# равным 'кнопочный'.
keypad_phone = Phone(dial_type_value='кнопочный')

# Печать значения атрибута класса.
print(rotary_phone.line_type)
# Печать значения атрибута объекта.
print(rotary_phone.dial_type)
# Печать значения атрибута класса.
print(keypad_phone.line_type)
# Печать значения атрибута объекта.
print(keypad_phone.dial_type)

# Выведется:
# проводной
# дисковый
# проводной
# кнопочный 