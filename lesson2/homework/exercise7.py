"""7. Реализовать проект «Операции с комплексными числами». Создайте
класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNumber:
    """ Класс для комплексных чисел
    """
    def __init__(self, comp_num: str):
        """ Принемает коплексные числа в виде строки типа 'числоi'

        :param comp_num: str
        """
        self.comp_num = comp_num
        try:
            self.number = int(self.comp_num.split('i')[0])
        except:
            print('Неправельно введено комплексное число')

    def __add__(self, other):
        return f'{self.number + other.number}i'

    def __mul__(self, other):
        return f'{self.number * other.number*-1}'


# Проверка
a = ComplexNumber('5i')
b = ComplexNumber('6i')
print(a+b)
print(a*b)