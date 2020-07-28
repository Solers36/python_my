"""В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра. 
В теле cylinder() определена функция circle(), вычисляющая площадь круга по формуле πr2. 
В теле cylinder() у пользователя спрашивается, хочет ли он получить только площадь боковой 
поверхности цилиндра, которая вычисляется по формуле 2πrh, или полную площадь цилиндра. 
В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат 
вычислений функции circle()."""

import math


def cylinder():
    def circle():
        area_circle = math.pi * radius**2
        return area_circle
    while True:
        try:
            radius = float(input("Радиус: "))
            height = float(input("Высота: "))
            break
        except ValueError:
            print("Используйте цифры.")

    while True:
        try:
            number = int(input(
                "Получить площадь боковой поверхности цилиндра - 1, полную площадь цилиндра - 2: "))
            if number == 1:
                area = 2 * math.pi * radius * height
                break
            elif number == 2:
                area = (2 * math.pi * radius * height) + 2 * circle()
                break
            else:
                raise ValueError()
        except ValueError:
            print("Используйте цифры 1 или 2.")
    print("Площадь: %.2f" % area)


cylinder()