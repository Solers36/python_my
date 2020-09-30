"""
Напишите класс Snow по следующему описанию.

В конструкторе класса инициируется поле, содержащее количество снежинок, 
выраженное целым числом.

Класс включает методы перегрузки арифметических операторов: __add__() – сложение, 
__sub__() – вычитание, __mul__() – умножение, __truediv__() – деление. В классе 
код этих методов должен выполнять увеличение или уменьшение количества снежинок на 
число n или в n раз. Метод __truediv__() перегружает обычное (/), а не целочисленное 
(//) деление. Однако пусть в методе происходит округление значения до целого числа.

Класс включает метод makeSnow(), который принимает сам объект и число снежинок в ряду, 
а возвращает строку вида "*****\n*****\n*****…", где количество снежинок между '\n' 
равно переданному аргументу, а количество рядов вычисляется, исходя из общего количества 
снежинок.

Вызов объекта класса Snow в нотации функции с одним аргументом, должен приводить к 
перезаписи значения поля, в котором хранится количество снежинок, на переданное в качестве 
аргумента значение.
"""
import math


class Snow:
    def __init__(self, number_of_snowflakes):
        self.number_of_snowflakes = int(number_of_snowflakes)

    def __add__(self, n):
        return self.number_of_snowflakes + n
    def __sub__(self, n):
        return self.number_of_snowflakes - n
    def __mul__(self, n):
        return self.number_of_snowflakes * n
    def __truediv__(self, n):
        return self.number_of_snowflakes // n
    def __call__(self, new_number):
        self.number_of_snowflakes = new_number

    def makeSnow(self, number_of_snowflakes_in_a_row):
        string_of_snowflakes = ""
        number_of_row = int(self.number_of_snowflakes)//number_of_snowflakes_in_a_row
        for i in range(number_of_row):
            string_of_snowflakes += ("*" * number_of_snowflakes_in_a_row)
            string_of_snowflakes += "\n"
        rest_of_snowflakes = (int(self.number_of_snowflakes) - number_of_row * number_of_snowflakes_in_a_row)
        string_of_snowflakes += "*" * rest_of_snowflakes
        return string_of_snowflakes


a = Snow(25)
print(a.makeSnow(8))