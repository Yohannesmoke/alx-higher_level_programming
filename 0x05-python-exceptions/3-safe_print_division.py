#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        value = int(a) / int(b)
    except:
        value = None
    finally:
        print("inside result: {}".format(value))
    return value
