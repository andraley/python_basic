"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов методы
должен выводить уникальное сообщение. Создать экземпляры классов
и проверить, что выведет описанный метод для каждого экземпляра.
 """

class Stationery:
    """ Описывает канцелярские принадлежности
    """
    def __init__(self, title:str):
        self.title = title
    def draw(self):
        print("Запуск отрисовки\n")

class Pen(Stationery):
    """ Описывает ручки
    """
    def draw(self):
        print("Рисуем ручкой\n")

class Pencil(Stationery):
    """ Описывает карандаши
    """
    def draw(self):
        print("Рисуем карандашом\n")

class Handle(Stationery):
    """ Описывает маркеры
    """
    def draw(self):
        print("Рисуем маркером\n")

# Проверка методов
my_stationery = Stationery('Erich Krause')
my_stationery.draw()

my_pen = Pen('Erich Krause')
my_pen.draw()

my_handle = Handle('Erich Krause')
my_handle.draw()

my_pencil = Pencil('Erich Krause')
my_pencil.draw()