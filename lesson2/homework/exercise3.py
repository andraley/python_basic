"""3. Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов. Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""


from pathlib import Path

file_name = 'exercise3.txt'

with open(Path(__file__).parent.joinpath(file_name),'r', encoding="UTF-8") as employee_file:
   employee_list = employee_file.read().split()   #Создание списка слов

#Создания словаря из списка (ключ=Фамили, значение=оклад
employee_dict = dict(zip(employee_list[::2], employee_list[1::2]))

#Перевод значений словоря в числовой формат
salary_dict = {surname: float(salary) for surname, salary in employee_dict.items()}

#Создание списка сотрудников с окладом меньше 20 тыс
salary_lowest = [surname for surname, salary in salary_dict.items() if salary < 20000]
print(f"Сотрудники имеющие зарплату меньше 20 тыс: {salary_lowest}")

#Посдсчет средней зарплаты
all_salaries = 0
for salary in salary_dict.values():
    all_salaries = (all_salaries + salary)
print(f"Средный оклад в компании: {all_salaries/len(salary_dict)}")