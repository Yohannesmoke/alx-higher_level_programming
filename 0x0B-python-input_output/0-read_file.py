#!/usr/bin/python3

"""Write a function that reads a text file
 (UTF8) and prints it to stdout:"""


def read_file(filename=""):

    """Write a function that reads a text file"""
    with open(filename,'r',encoding="utf-8") as my_file:
        for i in my_file:

            print(i, end="")
    my_file.closed
