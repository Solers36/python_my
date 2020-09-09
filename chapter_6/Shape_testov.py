"""
Измените класс Point (из модуля Shape.py или ShapeAlt.py) так, что>
бы обеспечить поддержку следующих операций, где p, q и r являют>
ся объектами типа Point, а n – число.
p = q + r # Point.__add__()
p += q # Point.__iadd__()
p = q ! r # Point.__sub__()
p != q # Point.__isub__()
p = q * n # Point.__mul__()
p *= n # Point.__imul__()
p = q / n # Point.__truediv__()
p /= n # Point.__itruediv__()
p = q // n # Point.__floordiv__()
p //= n # Point.__ifloordiv__()
Каждый из методов реализации комбинированных инструкций
присваивания будет состоять всего из четырех строк программного
кода, а все остальные методы – из двух, включая строку с инструк>
цией def, и, конечно же, все они очень просты и похожи между со>
бой. С минимальным описанием и доктестом для каждого из них
всего добавится порядка ста тридцати новых строк.
"""

"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


    def __add__(self, other):
        """Returns the result of adding the coordinates 
        of two points along the x and y axes
        >>> a = Point(1, 3)
        >>> b = Point(2, 4)
        >>> c = a + b
        >>> c
        Point(3, 7)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """Returns the changed coordinates by adding the x and y 
        values of the other point to them
        >>> a = Point(1, 3)
        >>> b = Point(2, 4)
        >>> a += b
        >>> a
        Point(3, 7)
        """
        self.x += other.x
        self.y += other.y
        return self


    def __sub__(self, other):
        """Returns the result of subtracting the coordinates 
        of two points along the x and y axes
        >>> a = Point(5, 3)
        >>> b = Point(2, 4)
        >>> c = a - b
        >>> c
        Point(3, -1)
        """
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        """Returns the changed coordinates by subtracting the x and y 
        values of the other point
        >>> a = Point(5, 3)
        >>> b = Point(2, 4)
        >>> a -= b
        >>> a
        Point(3, -1)
        """
        self.x -= other.x
        self.y -= other.y
        return self


    def __mul__(self, multiplier):
        """Returns the result of multiplying the point coordinates 
        along the x and y axes by a number
        >>> a = Point(5, 3)
        >>> b = a * 3
        >>> b
        Point(15, 9)
        """
        return Point(self.x * multiplier, self.y * multiplier)

    def __imul__(self, multiplier):
        """Returns the changed x and y coordinates multiplied by a number
        >>> a = Point(5, 3)
        >>> a =* 3
        >>> a
        Point(15, 9)
        """
        self.x *= multiplier
        self.y *= multiplier
        return self


    def __truediv__(self, divider):
        """Returns the result of dividing the point coordinates 
        along the x and y axes by a number
        >>> a = Point(8, 9)
        >>> b = a / 4
        >>> b
        Point(2.0, 2.25)
        """
        return Point(self.x / divider, self.y / divider)

    def __itruediv__(self, divider):
        """Returns the changed x and y coordinates divided by a number
        >>> a = Point(8, 9)
        >>> a /= 4
        >>> a
        Point(2.0, 2.25)
        """
        self.x /= divider
        self.y /= divider
        return self


    def __floordiv__(self, divider): 
        """Returns the result of integer division of the point 
        coordinates along the x and y axes by a number
        >>> a = Point(8, 9)
        >>> b = a // 4
        >>> b
        Point(2, 2)
        """
        return Point(self.x // divider, self.y // divider)

    def __ifloordiv__(self, divider):
        """Returns the changed x and y coordinates after integer 
        division by a number
        >>> a = Point(8, 9)
        >>> a //= 4
        >>> a
        Point(2, 2)
        """
        self.x //= divider
        self.y //= divider
        return self




class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return repr(self)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
