"""1. Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление. Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
 """


def my_division(my_devidend: float, my_divisor: float) -> float:
    """ Запрачивает у пользователя два числа и затем их делит

    :param my_devidend: int, float делиое
    :param my_divisor:  int, float делитель
    :return: float or str (при делении на ноль)
    """

    try:
        my_quotient = my_devidend / my_divisor
        return my_quotient
    except ZeroDivisionError: #Проверка на деление на ноль
        answer_div = 'Вы попытались поделить число на ноль'
        return answer_div



while True: #Проверка на правельность ввода
    try:
        user_devidend = float(input('Введите делимое:'))
        user_divisor = float(input('Введите делитель:'))
        break
    except ValueError:
        print('Не правельно заданы числа.')

#Вызов функции
user_quotient = my_division(user_devidend, user_divisor)

print(f'Ответ: {user_quotient:.4f}') #вывод даных