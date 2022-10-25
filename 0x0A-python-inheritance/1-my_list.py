#!/usr/bin/python3
"""the file for the question 0x01 that is answered in this section"""
class Mylist(list):
    """a child class that inherit the variables and functions of the parent class 
    and that is very helpful because the child class are very dependent on the parent 
    class"""
    def print_sorted(self):
        """a public instance method that will sort the given list in ascending 
        order and print it in a list form"""
        new_list = Mylist()
        for i in self:
            new_list.append(i)
        print(sorted(new_list))
