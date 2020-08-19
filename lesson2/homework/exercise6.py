"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо
предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle, islice


# Задача a

# Определение переменых
number_list = []
first_number = 23
last_number = 41

# Первый способ создания итератора чисел
def numbers (first_number:int, last_number: int) -> list:
    """Создаёт список чисел

    :param first_number: int
    :param last_number: int
    :return: list
    """
    for _ in count (first_number):
        if _ > last_number:
            break
        else:
            number_list.append(_)
    return number_list

print(numbers(first_number, last_number))   # Вывод списка созданого первым способом

# Второй способ создания итератора чисел
numbers_list2 = [_ for _ in islice(count(first_number), (last_number - first_number + 1))]

print(numbers_list2)    # Вывод списка созданого втормы способом



# Задача б

# Определение переменых
srt_list = []
user_str = 'GeekBrains'

# Первый способ создания итератора
def letters (user_str: str) -> list:
    """Создаёт список букв из принятой сторки

    :param user_str:
    :return:
    """
    for _ in  islice(cycle(user_str), len(user_str)):
        srt_list.append(_)
    return srt_list

print(letters('GeekBrains'))  # Вывод списка созданого первым способом

# Второй способ создания итератора
str_list2 = [_ for _ in islice(cycle(user_str), len(user_str))]

print(str_list2)    # Вывод списка созданого первым способом