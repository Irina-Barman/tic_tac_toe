from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()


# Запускается бесконечный цикл.
    while True:
        # В этом блоке содержатся значения, которые могут вызвать исключение.
        try:
            # Ползователь вводит номер строки.
            row = int(input('Введите номер строки: '))
            # Если введенное число меньше 0 или больше
            # или равно field_size...
            if row < 0 or row >= game.field_size:
                # ... и выбразывается собственное исключение FieldIndexError
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            if column < 0 or column >= game.field_size:
                raise FieldIndexError
        except FieldIndexError:
            print(
                'Значение добжно быть неотрицательным и меньше '
                f' {game.field_size}.'
            )
            print('Пожалуйста, введите значение для строки и столбца заново')
            continue
        except ValueError:
            print('Буквы вводить нельзя, только цифры')
            print('Пожалуйста, введите значение для строки и столбца заново')
        else:
            break

    game.make_move(0, 2, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()
