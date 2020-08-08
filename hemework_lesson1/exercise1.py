"""1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните
в переменные, выведите на экран.
"""

#Создание перемнных
first_var = 3
second_var = 3.33
third_var = 'string'
forth_var = False
fifth_var = [1, 2, 3, 'Hello world!']

#Вывод переменных
print('Первая переменная: ' + str(first_var) + '. Тип:' + str(type(first_var)))
print('Вторая переменная: ' + str(second_var) + '. Тип:' + str(type(second_var)))
print('Третья переменная: ' + third_var + '. Тип:' + str(type(third_var)))
print('Четвертая переменная: ' + str(forth_var) + '. Тип:' + str(type(forth_var)))
print('Пятая переменная: ' + str(fifth_var) + '. Тип:' + str(type(fifth_var)))

#Ввод новых переменных
word_var = input('Напишите любое слово ')
string_var = input('Напишите строку ')
number_var = input('Напишите целое число ')
float_var = input('Напишите дробное число ')


#Вывод новых переменных
print('Вы написали слово: ' + word_var)

print('Вы написали строку: ' + string_var)

if number_var.isdigit(): #Проверка является ли числом
    print('Вы написали число: ' + number_var)
else:
    print('Вы ошиблись в написании числа.')

try: #Проверка является ли числом
    if float(float_var):
        print('Вы написали число: ' + str(float_var))
except ValueError:
        print('Вы ошиблись в написании числа.')

