"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке.
"""

from pathlib import Path

file_name = 'exercise2.txt'

#Создание списка строк
with open(Path(__file__).parent.joinpath(file_name), 'r', encoding='UTF-8') as files_text:
    strings_list = files_text.read().split('\n')

print(f"Количество строк: {len(strings_list)}")

#Подсчёт количества стлов в каждой строке
lines = 1
for words in strings_list:
    print(f"Количество слов в строке {lines}: {len(words.split())}")
    lines +=1

