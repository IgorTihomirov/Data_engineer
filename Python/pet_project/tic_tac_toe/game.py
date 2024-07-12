from inspect import getsource
from gameparts import Board


# Вот новая функция.   
def main():

# Создать игровое поле - объект класса Board.
    game = Board()
# Отрисовать поле в терминале.
    game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(1, 2, 'X')
    print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
    game.display()


# А вот вызов этой функции.
if __name__ == '__main__':
    main()


game = Board()
print(getsource(Board)) 