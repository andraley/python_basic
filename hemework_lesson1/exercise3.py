"""3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

#Запрос числа
number = input('Введите число: ')

#Вывод суммы
print(f'Сумма {number} + {number}{number} '
      f'+ {number}{number}{number} равна: '
      f'{int(number) + int(number + number) + int(number + number + number)}')
