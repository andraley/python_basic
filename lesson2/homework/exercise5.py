"""5. Создать (программно) текстовый файл, записать в него
программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""


from pathlib import Path

nubmer_string = '1 2 3 4 5 6 7 8 9'

with open('exercise5.txt', 'w', encoding='UTF-8') as writing_file:
    writing_file.write(nubmer_string)

# Создаётся список числе (формат float) из записаного файла
with open(Path(__file__).parent.joinpath('exercise5.txt')) as reading_file:
    nurber_list = [float(numbers) for numbers in reading_file.read().split()]

print(f"Сумма чисел = {sum(nurber_list)}")