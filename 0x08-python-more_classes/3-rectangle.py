#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 0 if self.__height == 0 or self.__width == 0 else 2 * (self.__height + self.__width)

    def __str__(self):
        """Return string representation of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return '\n'.join(['#' * self.__width for _ in range(self.__height)])

