"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionZeroError(Exception):

    @staticmethod
    def division():
        """ Функция для деления.
        При попытке деление на ноль печатает предупреждение.
        :return: float
        """
        try:
            __dividend = float(input('Введите делимое:'))
            __divisor = float(input('Введите делитель:'))
            return __dividend/__divisor
        except ZeroDivisionError:
            print('Деление на ноль.')
        except ValueError:
            print('Не правельно введены числа.')

# Проверка
print(DivisionZeroError.division())


