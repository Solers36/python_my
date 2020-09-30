import math


class Win_Door:
    """Class Win_Door.Accepts the width and height of the door(window)."""
    def __init__(self, x, y):
        self.square = x * y


class Room:
    """Class Room. The constructor accepts width, length, and height."""
    def __init__(self, x, y, z):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def getSquare(self):
        """Returns the area of the room."""
        self.square = 2 * self.height * (self.width + self.lenght)
        return self.square

    def NumberOfRolls(self, x, y):
        """Returns the number of Wallpaper rolls required for pasting the room. 
        Accepts the length and width of the roll."""
        return math.ceil(self.getSquare() / (x * y))

    def addWD(self, w, h):
        """Adds a new object of the Win_Door class to the list. 
        Accepts the width and height of the door(window)."""
        self.wd.append(Win_Door(w, h))

    def workSurface(self):
        """Returns the area of the room without the area of Windows and doors."""
        new_square = float(self.getSquare())
        for i in self.wd:
            new_square -= i.square
        return new_square
