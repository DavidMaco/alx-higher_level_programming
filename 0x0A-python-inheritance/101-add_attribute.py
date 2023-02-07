#!/usr/bin/python3
"""Function that adds a new attribute to an object."""

def add_attribute(obj, name, value):
    """Raise a TypeError if the object can’t have new attribute."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
