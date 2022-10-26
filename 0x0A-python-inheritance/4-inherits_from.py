#!/usr/bin/python3
"""a file comment for the module of the 4-inherits file"""
def inherits_from(obj, a_class):
    if isinstance(obj, a_class):
        return obj.__class__ is not a_class
    else:
        return False   
    """returns True if the object is an instance of a
      class that inherited (directly or indirectly) 
      from the specified class ; otherwise False.
      """
