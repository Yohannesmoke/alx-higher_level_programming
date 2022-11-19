#!/usr/bin/python3
"""
this is the "0-add_integer" module.
this module help to add to integers and return their sum
"""
def add_integer(a, b=98):
   """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """ 
    if not isinstance(a, (int, float)):raise TypeError("a must be an integer ")
    if not isinstance(b, (int, float)):raise TypeError("b must be an integer ")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
