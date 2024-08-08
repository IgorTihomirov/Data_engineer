import random


class MarsURLEncoder:

    def __init__(self):
        self.charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.urls = {}

    def generate_hash(self):
        """Генерирует уникальный хеш из 6 случайных символов."""
        while True:
            new_hash = ''  # Инициализация пустой строки для хеша
            for _ in range(6):
                random_symbol = random.choice(self.charset)  # Выбираем случайный символ
                new_hash += random_symbol  # Добавляем выбранный символ к хешу
            if new_hash not in self.urls:  # Проверка на уникальность
                return new_hash

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        # Генерируем уникальный хеш
        unique_hash = self.generate_hash()

        # "Связываем" уникальный хэш с оригинальным URL
        self.urls[unique_hash] = long_url

        # Формируем зашифрованный URL
        code_url = f"https://ma.rs/{unique_hash}"    
        return code_url

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        # Разделяем ссылку под знаку "/". 
        # Получаем список строк и берем из списка последний элемент,
        #  то есть хэш
        delete_hash = short_url.split("/")[-1]

        # Ищем оригинальный URL по короткому хешу
        return self.urls.get(delete_hash)
