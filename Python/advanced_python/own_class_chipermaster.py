class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
   
    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст 
        # с учетом переданного смещения shift.
        cipher_txt = ''
        self.text_lower = original_text.lower()
        for element in self.text_lower:
            if element in self.alphabet:
                cipher_txt = cipher_txt + self.alphabet[(self.alphabet.find(element) + shift) % len(self.alphabet)]
            else:
                cipher_txt += element
        return cipher_txt
   
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        cipher_txt = ''
        self.text_lower = cipher_text.lower()
        for element in self.text_lower:
            if element in self.alphabet:
                cipher_txt = cipher_txt + self.alphabet[(self.alphabet.find(element) - shift) % len(self.alphabet)]
            else:
                cipher_txt += element
        return cipher_txt


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))