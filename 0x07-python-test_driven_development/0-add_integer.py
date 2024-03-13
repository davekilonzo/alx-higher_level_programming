#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add 2 integers.

    Prototype: def add_integers(a, b=98)
    a and b must be integers or floats
    if not, raise a TypeError exception
    Return: returns the sum of a and b
    """
    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except(ValueError, TypeError):
        raise TypeError("b must be an integer")

    return a + b
