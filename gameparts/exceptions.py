class FieldIndexError(IndexError):
    def __str__(self):
        return 'Введено значение за границами игрового поля'


class GvalueError(ValueError):
    def __str__(self):
        return 'Введены буквы'
