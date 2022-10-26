#!/usr/bin/python3
"""Write a class BaseGeometry"""


class BaseGeometry:
    """a class that is based on the previous class"""
    def area(self):
        """that raises an Exception with the message """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """that validates value:you can assume name is always a string
        if value is not an integer: raise a TypeError exception, with the
        message <name> must be an integer if value is less or equal to 0:
        raise a ValueError exception with the message <name> must be 
        greater than 0
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if (value <= 0):raise ValueError("{} must be greater than 0".format(self.name))
