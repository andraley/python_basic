"""7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).

Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from pathlib import Path
import json

file_nime = 'exercise7_in.txt'

# Создание многомерного списка коппаний
companies = []
with open(Path(__file__).parent.joinpath(file_nime), 'r', encoding='UTF-8') as companies_file:
    for lines in companies_file:
       companies.append(lines.split())

# Создание словаря из компаний с их прибылями(убытками
profit_companies = 0
all_profit = 0
companies_dict = {}
for tmp in companies:
    company_name = tmp[0]
    profit = int(tmp[2]) - int(tmp[3])
    if profit >= 0:
        all_profit += profit    # Подсчет общей прыбыли всех компаний
        profit_companies += 1   # Подсчет количества прибыльных компаний
    companies_dict.update({company_name: profit})

# Подсчет средней прибыли компаний и создания словаря
avr_profit = all_profit/profit_companies
avr_prf_dict = {"average_profit": avr_profit}

# Обединение словарей в список
companies_list = [companies_dict, avr_prf_dict]

# Создания файла со списоп из словарей в json формате
with open('exercise7_out.txt', 'w', encoding='UTF-8') as dict_file:
    json.dump(companies_list, dict_file, ensure_ascii=False)


