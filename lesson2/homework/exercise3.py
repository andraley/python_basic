"""3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на
реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """" Описывает данные о работнике
    """
    def __init__(self, name: str, surname: str, position:str, wage: float, bonus: int):
        """ Принимает данные о работнике

        :param name: str
        :param surname: str
        :param position: str
        :param wage: float
        :param bonus: int
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"оклад": wage, "бонус": bonus}

class Position(Worker):
    """ Выводит данные о работнике

    """
    def __init__(self, name: str, surname: str, position:str, wage: float, bonus: int):
        """ Принимает атрибуты у материнского класа WorkerS

        :param name: str
        :param surname: str
        :param position: str
        :param wage: float
        :param bonus: int
        """
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self) ->str:
        """ Выводит фамилию и имя сотрудника

        :return: str
        """
        self.full_name = self.surname + " " + self.name
        return self.full_name

    def get_total_income(self) -> float:
        """ Выводит доход сотрудника

        :return: float
        """
        self.total_income = self._income["оклад"] + self._income["бонус"]
        return self.total_income


# Проверка данных
employee = Position('Alex', 'Wi', 'boss', 1000, 100)
print(employee.name)
print(employee.surname)
print(employee.position)
print(employee._income)
print(employee.get_full_name())
print(employee.get_total_income())