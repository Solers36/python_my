import math


class Win_Door:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def getSquare(self):
        self.square = 2 * self.height * (self.width + self.lenght)
        return self.square

    def NumberOfRolls(self, x, y):
        return math.ceil(self.getSquare() / (x * y))

    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))

    def workSurface(self):
        new_square = float(self.getSquare())
        for i in self.wd:
            new_square -= i.square
        return new_square
