"""3. Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу исключения
на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список. Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду
“stop”. При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только
числа и строки. При вводе пользователем очередного элемента необходимо
реализовать проверку типа элемента и вносить его в список, только если
введено число. Класс-исключение должен не позволить пользователю ввести
текст (не число) и отобразить соответствующее сообщение. При этом работа
скрипта не должна завершаться.
"""

class CheckingListError(Exception):
    def __init__(self, text):
        self.text =text


user_list=[]
print('Введите числа.')
while True:
    new_number = input('Для прекращение ввода введите "stop".\n')
    try:
        if new_number.isdigit():
            user_list.append(int(new_number))
        elif new_number == 'stop':
            print(user_list)
            break
        else:
            raise CheckingListError('Вы ошиблись в воде числа.')
    except CheckingListError as text:
        print(text)








