В папке tic_tac_toe создайте файл game.py. В нём вы и начнёте писать код игры.
Класс, который опишет поле игры «Крестики-нолики», должен как минимум:
Хранить состояние поля.
Содержать метод, который будет обрабатывать ходы игроков.
Содержать метод, который будет отрисовывать поле.

Игровое поле можно представить как список списков со строками в виде пробела. 
Каждая строка — пустая клетка. 

Инициализация игрового поля может происходить в инициализаторе класса, в атрибуте board.

Для метода, который будет обрабатывать ходы игроков, подойдёт название make_move(). 
Этот метод должен отвечать за размещение нужного символа в выбранной клетке 
(в списке board). Для этого он должен:
принимать координаты поля;
принимать символ — крестик или нолик;
размещать этот символ на поле.

За отрисовку поля может отвечать метод с названием display(). 

Поле с содержимым клеток можно отрисовать прямо в терминале, 
а строки из списка board могут разделяться вертикальной чертой, 
чтобы поле визуально лучше воспринималось. 
На основе такого описания получится следующий код: