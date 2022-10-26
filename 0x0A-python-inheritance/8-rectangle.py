#!/usr/bin/python3
"""a class that is based on the previous class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height) -> None:
        """width and height must be private. No getter or setter
        width and height must be positive integers, validated by
         integer_validator
         """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
