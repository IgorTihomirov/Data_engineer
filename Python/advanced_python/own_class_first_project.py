class Employee:
    # Атрибут класса.
    vacation_days = 28
    _employee_id = ''

    # Это инициализатор/конструктор класса, в котором объявлено два параметра.
    def __init__(self, first_name, second_name, gender):
        # first_name, second_name, gender - атрибут объекта
        # first_name_value, second_name_value, gender_value - значение для атрибута объекта
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self._employee_id = self.__generate_employee_id()

    def consume_vacation(self, free_vacation_days_value):
        self.remaining_vacation_days -= free_vacation_days_value

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    
    def __generate_employee_id(self):
        self._employee_id = hash(
            self.first_name + self.second_name + self.gender)
        return self._employee_id


class FullTimeEmployee(Employee):
    __salary = ''

    def get_unpaid_vacation(self, date_unpaid_vacation, amount_days):
        self.date_unpaid_vacation = date_unpaid_vacation
        self.amount_days = amount_days
        return f'Начало неоплачиваемого отпуска: {self.date_unpaid_vacation}, продолжительность: {self.amount_days} дней.'
    
    def __init__(self, first_name, second_name, gender, __salary):
        super().__init__(first_name, second_name, gender)
        self.__salary = __salary

    def __get_vacation_salary(self):
        self.__salary *= 0.8
        return float(self.__salary)


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


# Пример использования:
full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
