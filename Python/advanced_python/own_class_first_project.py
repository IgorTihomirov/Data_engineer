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
        return f'Остаток отпускных дней: {self.remaining_vacation_days}'
      

# Пример использования класса:
employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())
