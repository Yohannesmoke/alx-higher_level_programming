#!/usr/bin/python3
"""This module  has a class for rectangule instances.
The module has the class Rectangle.
"""
import re
from turtle import width


class Rectangle:
    """class rectangle.
    the class defines the height and width prived
    instance attributes, getter and setter method for each.
    area and permiter methods
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:    
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        else:
            return 2 * self.height + 2 * self.width
    def __str__(self):
        if(self.height != 0 and self.width != 0):
            a = self.width * "#" + "\n"
            b = self.height * "#"
            return ((self.height - 1) * a + b)
        else:
            return ("")
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) is not int:raise TypeError("width must be an integer")
        
        elif value < 0:raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:raise TypeError("width must be an integer")
        
        if value < 0:raise ValueError("width must be >= 0")
        else:
            self.__height = value
