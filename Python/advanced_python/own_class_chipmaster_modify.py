class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
   
    def process_text(self, text, shift, is_encrypt):
        if is_encrypt is True:
            txt = ''
            self.text_lower = text.lower()
            for element in self.text_lower:
                if element in self.alphabet:
                    txt = txt + self.alphabet[(self.alphabet.find(element) + shift) % len(self.alphabet)]
                else:
                    txt += element
            return txt
        else:
            txt = ''
            self.text_lower = text.lower()
            for element in self.text_lower:
                if element in self.alphabet:
                    txt = txt + self.alphabet[(self.alphabet.find(element) - shift) % len(self.alphabet)]
                else:
                    txt += element
            return txt    


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
