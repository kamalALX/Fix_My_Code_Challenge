#!/usr/bin/python3
""" this module defines a class named square """


class Square():
    """ class square that creates a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ class square that creates a square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ class square that creates a square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ class square that creates a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creates Square object."""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
