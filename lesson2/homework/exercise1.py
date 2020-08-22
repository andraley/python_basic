"""1. Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
"""

from sys import argv

_, surname, name, hours, salary_rate, bonus = argv  #Присваение переменым значения из терминала


def salary (surname: str, name: str, hours: int, salary_rate: float, bonus: int) -> dict :
    """Растчитывет заработную плату сотрудника

    :param surname: str   Фамилия сотрудника
    :param name: str    Имя сотрудника
    :param hours: int   Выработка в часах сотрудника (натуральное число)
    :param salary_rate: float   ставка в час сотрудника (положительное)
    :param bonus: int, float Премия сотрудника (Для штрафа использовать отрицательное число)
    :return: dict   Возвращает словарь (ключ - ФИ сотрудника, значение - зарплата)
    """
    try:   #Проверка правельности ввода значений
        hours = float(hours)
        salary_rate = float(salary_rate)
        bonus = float(bonus)
    except ValueError:
        print('Ошибка ввода')
        exit()

    if (hours or salary_rate) < 0:  #Проверка правельности ввода значений
        print('Ошибка ввода даных о зарплате')
        return {surname + ' ' + name: -1}

    return {surname + ' '+ name: hours * salary_rate + bonus}


print(salary(surname, name, hours, salary_rate, bonus))  #Вывод заработной платы сотрудника
