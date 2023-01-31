#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the instance."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """method that returns the value of the width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Get/set the width."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Get/set the height."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    
    def area(self):
        """Calculate the Rectangle area."""

        return self.width * self.height

    def perimeter(self):
        """Calculate the Rectangle perimeter."""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
