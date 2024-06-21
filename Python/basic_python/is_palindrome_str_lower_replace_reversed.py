def is_palindrome(sequence):
    # Ваш код здесь
    lower_sequence = str.lower(sequence)
    replace_lower_sequence = str.replace(lower_sequence, ' ', '')
    reverse_sequence = replace_lower_sequence[::-1]
    if reverse_sequence == replace_lower_sequence:
        return True
    else: return False


# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))