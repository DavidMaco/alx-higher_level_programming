#!/usr/bin/python3
"""Define a functiin for an instance of a class"""

def inherits_from(obj, a_class):
    """Returns True/False if obj is an instance of a_class."""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
