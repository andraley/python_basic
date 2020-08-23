"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from pathlib import Path

file_name = 'exercise4_in.txt'

# Создания списка строк из файла
lines_list = []
with open(Path(__file__).parent.joinpath(file_name),'r', encoding="UTF-8") as numbers_file:
   for line in numbers_file:
       lines_list.append(line)

# Создания нового списка с русскими числительными
russian_numbers = ["Один ", "Два ", "Три ", "Четыри "]
new_list = []
for i, string in enumerate(lines_list):
   position = string.find('—')
   new_line = russian_numbers[i] + string[position:]
   new_list.append(new_line)

# Запись нового файла с русскими числительными
with open('exercise4_out.txt', 'w') as text_file:
    text_file.writelines(new_list)