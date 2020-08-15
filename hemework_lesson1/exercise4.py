"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
#Запрашиваем чисто
user_number = int(input('Введите число: '))

#Вводим переменную для максимальной цифры
max_figure = 0

#Создаём цикл проверки цифр в числе
while user_number:
    figure = user_number % 10
    user_number = user_number // 10
    if figure > max_figure:
        max_figure = figure

#Выводим цифру в числе
print(f'Макcимальная цифра в числе: {max_figure}')