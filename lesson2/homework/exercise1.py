"""1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках класса
реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.
"""

class Date:
    def __init__(self, date: str):
        self.date = date


    @classmethod
    def numbers_date(cls, date: str)->list:
        """ Преобразоввывает стоку с датой в числовой формат

        :param date: str
        :return: list
        """
        list_numbers = list(map(int, (date.split('-'))))
        return list_numbers

    @staticmethod
    def check_date(date:str):
        """ Проверяет правельность указание даты в строке

        :param date: str
        :return:
        """
        list_numbers = list(map(int, (date.split('-'))))

        if list_numbers[1] < 1 or list_numbers[1] > 12:
            raise ValueError('Ошибка при вводе месяца')
        if list_numbers[2] < 0:
            raise ValueError('Ошибка при вводе года')
        if list_numbers[0] < 1:
            raise ValueError('Ошибка при вводе дня')
        if list_numbers[1] == 2:

            if list_numbers[0] > 29:
                raise ValueError('Ошибка при вводе дня')
            if list_numbers[2]%4 and list_numbers[0] > 28:
                    raise ValueError('Ошибка при вводе дня')

        if list_numbers[1] in [1, 3, 5, 7, 8, 10 ,12]:
            if list_numbers[0] > 31:
                raise ValueError('Ошибка при вводе дня')
        else:
            if list_numbers[0] > 30:
                raise ValueError('Ошибка при вводе дня')


a = Date('10-11-2008')
print(Date.numbers_date('10-11-2008'))
a.check_date('10-11-2008')







