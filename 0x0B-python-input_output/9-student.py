#!/usr/bin/python3
"""Write a class Student that defines a student by:"""
class Student:
    """Public instance attributes:
first_name
last_name
age
"""


    def __init__(self, first_name, last_name, age) -> None:
        """Instantiation with first_name, last_name """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """that retrieves a dictionary representation of a Student"""
        return(self.__dict__)
