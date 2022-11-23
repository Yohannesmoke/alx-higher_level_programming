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
	super().__init__(size, size, x, y, id)
	self.size = size

    def __str__(self):
        """overloading __str__ method """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)    
