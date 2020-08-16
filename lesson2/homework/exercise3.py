"""3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func (number1 : float, number2: float, number3: float ) -> float :
    """ Суммирует два наибольших числа из трех
    :param number1: int, float
    :param number2: int, float
    :param number3: int, float
    :return: int, float
    """
    biggest_sum = number1 + number2 + number3 - min(number1, number2, number3)
    return biggest_sum

#Проверка функции
print(my_func(1, 2, 3))
print(my_func(2, 3, 1))
print(my_func(3, 1, 2))
print(my_func(1, 3, 1))
print(my_func(2, 2, 2))
