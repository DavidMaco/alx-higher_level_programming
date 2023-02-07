#!/usr/bin/python3
"""Define a class MyList."""

class MyList(list):
    """Sort the list in ascending order."""

    def print_sorted(self):
        """Method that prints the sorted list."""
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
