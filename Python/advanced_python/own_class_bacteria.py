class BacteriaProducer:
    # Допишите инициализатор класса
    def __init__(self, max_bacteria):
        self.bacterias = 0
        self.max_bacteria = max_bacteria

    # Допишите метод
    def create_new(self):
        if self.bacterias == self.max_bacteria:
            print('Нет места под новую бактерию')
        else: 
            self.bacterias += 1
            print(
                f'Добавлена одна бактерия. Количество бактерий в популяции: {self.bacterias}')


    # Допишите метод
    def remove_one(self):
        if self.bacterias == 0:
            print('В популяции нет бактерий, удалять нечего')
        else: 
            self.bacterias -= 1
            print(
                f'Одна бактерия удалена. Количество бактерий в популяции: {self.bacterias}')



# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
