#!/usr/bin/python3
"""
the class square that inherits from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """method initialization"""
	super().__init__(self, size, size, x, y, id)
	self.size = size
    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
    def __str__(self):
        """overloading __str__ method """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
