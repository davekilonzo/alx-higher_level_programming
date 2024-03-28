#!/usr/bin/python3
""" Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """creates class that defines a rectangle
    Attributes:
    empty
    """

    def __init__(self, width=0, height=0):
        """ method to initialize a Rectangle

        Attribute:
            width (int): optional, 0 by default
            height (int): optional, 0 by default
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets width

        Returns:
            width (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width of the rectangle

        Attributes:
            width (int)

        Raises:
            TypeError: width is not an integer
            ValueError: width is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        gets height
        Returns:
            height (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height of the rectangle

        Attributes:
            height (int)

        Raises:
            TypeError: height is not an integer
            ValueError: height is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
