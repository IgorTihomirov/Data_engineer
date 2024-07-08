class Employee:
    # Атрибут класса.
    vacation_days = 28

    # Это инициализатор/конструктор класса, в котором объявлено два параметра.
    def __init__(self, first_name_value, second_name_value, gender_value):
        # first_name, second_name, gender - атрибут объекта
        # first_name_value, second_name_value, gender_value - значение для атрибута объекта
        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value


# Создаем экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name_value='Сеня',
                     second_name_value='Петух', gender_value='м')
employee2 = Employee(first_name_value='Игорь',
                     second_name_value='Не Петух', gender_value='м')


# Вывод информации о сотрудниках.
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {
      employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {
      employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')
