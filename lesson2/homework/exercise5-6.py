"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад
оргтехники» максимум возможностей, изученных на уроках по ООП.
"""



class DeviceError(Exception):
    """ Класс для ошибки в случае неправельного заполнения данных
    """
    def __init__(self):
        print("Ошибка!Не правильный ввод данных.")

class Storage:
    """ Класс склада
    """
    __diveces_dict = {'принтер': 0, 'сканер': 0, 'мфу': 0}
    __storage_log = []

    @classmethod
    def add_to_storage(cls, name: str, amount: int):
        """Добавляет на склад оборудование

        :param name: str
        :param amount: int (целое положинельнное)
        :return:
        """
        name = name.lower()
        if not name in cls.__diveces_dict.keys() or amount < 0 or amount*10%10:
            raise DeviceError
        cls.__diveces_dict[name] = cls.__diveces_dict[name] + amount
        cls.__storage_log.append((name, amount))

    @classmethod
    def go_to_smwhr(cls, name: str, amount: int, direction: str):
        """ Оправляет со склада оборудование

        :param name: str
        :param amount: int
        :param direction: str
        :return:
        """
        name = name.lower()
        if not name in cls.__diveces_dict.keys() \
            or amount < 0 or amount * 10 % 10 or not type(direction) is str:
            raise DeviceError
        if cls.__diveces_dict[name] - amount >= 0:
            cls.__diveces_dict[name] = cls.__diveces_dict[name] - amount
            cls.__storage_log.append((name, amount, direction))
        else:
            print('На складе не достаточно оборудавния')

    @staticmethod
    def check_storage():
        """Проверка склада"""
        return Storage.__diveces_dict

    @staticmethod
    def create_storage_log():
        """Создание лога перемещения оборудования"""
        with open('storage_log.txt', 'w', encoding='UTF-8') as file_log:
            for tmp in Storage.__storage_log:
                file_log.write(f'{tmp}\n')

# Проверка
Storage.add_to_storage('принтер', 1)
Storage.add_to_storage('СкАнЕр', 5)
Storage.add_to_storage('МФУ', 3)
print(Storage.check_storage())

Storage.go_to_smwhr('Принтер', 2, 'кухня')
Storage.go_to_smwhr('сканер', 4, 'приёмная')
Storage.go_to_smwhr('МФУ', 3, 'офис')
print(Storage.check_storage())

Storage.create_storage_log()


