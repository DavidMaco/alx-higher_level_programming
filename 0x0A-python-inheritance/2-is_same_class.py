#!/usr/bin/python3
"""Define a funtion to check same instance."""

def is_same_class(obj, a_class):
    """Return true if an instance of specified class, otherwise false."""

    return type(obj) is a_class
