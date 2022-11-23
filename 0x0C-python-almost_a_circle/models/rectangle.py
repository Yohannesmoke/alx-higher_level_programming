#!/usr/bin/python3
""" define class rectangle """
from .base import Base


class Rectangle(Base):
    """ import class base inherit """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @property
    def height(self):
        """ getter """
        return self.__height

    @property
    def x(self):
        """ getter """
        return self.__x

    @property
    def y(self):
        """ getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area definer """
        return self.__width * self.__height

    def display(self):
        """define display"""
        rectangle = ""
        symbol = "#"
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            rectangle += (" " * self.__x) + (symbol * self.__width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """  overriding the __str__ method """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args):
        """define update"""
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass
