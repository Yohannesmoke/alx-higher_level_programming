#!/usr/bin/python3
"""
write Write a function that writes a string to a text file
(UTF8) and returns the number of characters
"""


def write_file(filename="", text=""):
    """
    write and encoding operation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
