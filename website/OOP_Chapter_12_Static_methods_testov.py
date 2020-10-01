"""
Приведенный в конце урока пример плохой. Мы можем менять значения полей dia и h 
объекта за пределами класса простым присваиванием (например, a.dia = 10). При 
этом площадь никак не будет пересчитываться. Также мы можем назначить новое значение 
для площади, как простым присваиванием, так и вызовом функции make_area() с последующим 
присваиванием. Например, a.area = a.make_area(2, 3). При этом не меняются высота и диаметр.

Защитите код от возможных логических ошибок следующим образом:

Свойствам dia и h объекта по-прежнему можно выполнять присваивание за пределами класса. 
Однако при этом "за кулисами" происходит пересчет площади, т. е. изменение значения area.

Свойству area нельзя присваивать за пределами класса. Можно только получать его значение.
"""


from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high
        self.__area = self.make_area(diameter, high)

    def __setattr__(self, attr, value):
        if attr in ('dia', 'h', '_Cylinder__area'):
            self.__dict__[attr] = value
            if self.__area != None:
                self.__dict__['_Cylinder__area'] = self.make_area(
                    self.dia, self.h)
        else:
            raise AttributeError

    def __getattr__(self, attr):
        if attr == 'area':
            return self.__area


a = Cylinder(1, 2)
print(a.area)

print(a.make_area(2, 2))
print(a.area)
a.dia = 2
a.h = 4
print(a.area)
print(a.dia, a.h)
