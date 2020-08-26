"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    """ Описыает параметры машины
    """
    def __init__(self, speed: float, color: str, name: str, is_polise: bool):
        """ принемает параметры машины

        :param speed: float (положительная
        :param color: str
        :param name: str
        :param is_polise: bool
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print("Машина поехала")

    def stop(self):
        self.speed = 0
        print("Машина остановлась")

    def turn(self, direction: str):
        """ Выводит в каком направлении машина повернула

        :param direction: str
        :return:
        """
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f"Скорость машины {self.speed} км/ч")

class TownCar(Car):
    """ Описыает параметры городской машинымашины
    """

    def __init__(self, speed: float, color: str, name: str, is_polise: bool):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        """ Выводить в скорость машины.
        Предупреждает если скороть больше допустимой.
        :return:
        """
        print(f"Скорость машины {self.speed} км/ч")
        if self.speed > 60:
            print(f"У вас слишком высокая скорость. Пожалуйста притормозите.")

class SportCar(Car):
    """ Описыает параметры спортивной машинымашины
    """
    def __init__(self, speed: float, color: str, name: str, is_polise: bool):
        super().__init__(speed, color, name, is_polise)

class WorktCar(Car):
    """ Описыает параметры рабочей машинымашины
    """
    def __init__(self, speed: float, color: str, name: str, is_polise: bool):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        """ Выводить в скорость машины.
        Предупреждает если скороть больше допустимой.
        :return:
        """
        print(f"Скорость машины {self.speed} км/ч")
        if self.speed > 40:
            print(f"У вас слишком высокая скорость. Пожалуйста притормозите.")

class PoliceCar(Car):
    """ Описыает параметры полицейской машинымашины
    """
    def __init__(self, speed: float, color: str, name: str, is_polise: bool):
        super().__init__(speed, color, name, is_polise)

# Проверка данных о гододской машине
priora = TownCar(55, 'violet', 'Lada', False)
priora.go()
print(priora.speed, priora.color, priora.name, priora.is_polise)
priora.turn('направо')
priora.show_speed()
priora.stop()
priora.show_speed()
print()

# Проверка данных о стортивной машине
ferrari = SportCar(100, 'red', 'California', False)
ferrari.go()
print(ferrari.speed, ferrari.color, ferrari.name, ferrari.is_polise)
ferrari.turn('налево')
ferrari.show_speed()
ferrari.stop()
print()

# Проверка данных о рабочей машине
ford = WorktCar(60, 'white', 'Transit', False)
ford.go()
print(ford.speed, ford.color, ford.name, ford.is_polise)
ford.turn('назад')
ford.show_speed()
ford.stop()
print()

# Проверка данных о полицейской машине
uaz = PoliceCar(80, 'white-blue', 'Patriot', True)
uaz.go()
print(uaz.speed, uaz.color, uaz.name, uaz.is_polise)
uaz.turn('за Фордом Транзитом ')
uaz.show_speed()
uaz.stop()
