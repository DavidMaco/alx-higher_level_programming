#!/usr/bin/python3
"""Define a class BaseGeometry."""

class BaseGeometry:
    """Define the attributes of Geometric Shapes."""

    def area(self):
        """Define the area of a geomtric shape."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that recieves the value property."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
