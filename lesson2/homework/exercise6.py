"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и
их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название
предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from pathlib import Path

file_nime = 'exercise6.txt'

# Создание списка строк из файла
with open(Path(__file__).parent.joinpath(file_nime), 'r', encoding='UTF-8') as courses_file:
    lines = courses_file.readlines()

# Создание списка названий предметов
name_courses = []
hours= []
for tmp in lines:
    position = tmp.find(':')
    name_courses.append(tmp[:position:])
    hours.append(tmp[position+2:])  # Удерает лишние части в сторке

# Создание списка суммарного количества часов
subject_hours_str = []
courses_hours = []
for tmp_2 in hours:
    sepatated = tmp_2.split()
    for tmp_3 in sepatated:  # Созание подсписка с количесвом часов в каждам элементе
        position_2 = tmp_3.find('(')
        subject_hours_str.append(tmp_3[:position_2:])
        subject_hours_int = [int(hour) for hour in subject_hours_str if hour]
    sum_hours = sum(subject_hours_int)
    courses_hours.append(sum_hours)
    subject_hours_str= []   # Очистка подсписка

# Обёдинение двух списков
courses_dict = dict(zip(name_courses, courses_hours))

print(courses_dict)

