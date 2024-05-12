#!/usr/bin/python3
""" this module defines a class named square """


class square():
    """ class square that creates a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ class square that creates a square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ class square that creates a square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ class square that creates a square """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ class square that creates a square """
    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
