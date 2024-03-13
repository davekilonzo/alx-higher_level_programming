#!/usr/bin/python3
"""
    this function adds 2 numbers
    if the numbers arent int or float
    raise a TypeError
    otherwise, return the sum
"""


def add_integer(a, b=98):
    """ add two integers or floats """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
