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
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, free_vacation_days_value):
        self.remaining_vacation_days -= free_vacation_days_value

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self, date_unpaid_vacation, amount_days):
        self.date_unpaid_vacation = date_unpaid_vacation
        self.amount_days = amount_days
        return f'Начало неоплачиваемого отпуска: {str(self.date_unpaid_vacation)}, продолжительность: {self.amount_days} дней.'


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name_value, second_name_value, gender_value):
        super().__init__(first_name_value, second_name_value, gender_value)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())
