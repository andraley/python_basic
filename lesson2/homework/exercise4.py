"""4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self):
        pass

class Devices:
    def __init__(self, name: str, price: float, size: int):
        """ Принемает параметры оргтехники

        :param name: str
        :param price: float
        :param size: int
        """
        self.name = name
        self.price = price
        self.size = size

class Printer(Devices):
    def __init__(self, colorful: bool, speed: float, name: str, price: float, size: int):
        """ Принемает параметры принтера

        :param colorful: bool
        :param speed: float
        """
        self.colorful = colorful
        self.speed = speed
        super().__init__(name, price, size)

    def __str__(self):
        return f'Принтер: "{self.name}"\nЦена: {self.price} руб\nРазмер: {self.size} см\n' \
               f'Цветной: {"да" if self.colorful else "нет"}\nСкорость: {self.speed} стр/мин\n'

class Scanner(Devices):
    def __init__(self, resolution: int, name: str, price: float, size: int):
        """ Принемает параметры принтера

        :param resolution: int
        """
        self.resolution = resolution
        super().__init__(name, price, size)

    def __str__(self):
        return f'Сканер: "{self.name}"\nЦена: {self.price} руб\nРазмер: {self.size} см\n' \
               f'Разрешение: {self.resolution} dpi\n'

class Copier(Devices):
    def __init__(self, colorful: bool, speed: float, resolution: int, name: str, price: float, size: int):
        """ Принемает параметры принтера

        :param colorful: bool
        :param speed: float
        :param resolution: int
        """
        self.colorful = colorful
        self.speed = speed
        self.resolution = resolution
        super().__init__(name, price, size)

    def __str__(self):
        return f'МФУ: "{self.name}"\nЦена: {self.price} руб\nРазмер: {self.size} см\n' \
               f'Цветной: {"да" if self.colorful else "нет"}\nСкорость: {self.speed} стр/мин\n' \
               f'Разрешение: {self.resolution} dpi\n'

hp_1234 = Printer(False, 30, 'HP', 4000, 200)
print(hp_1234)
cannon_1111 = Scanner(2000, 'Cannon', 1000, 100)
print(cannon_1111)
lg_98 = Copier(True, 15, 1500, 'LG', 9000, 300)
print(lg_98)