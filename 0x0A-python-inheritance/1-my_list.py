#!/usr/bin/python3
"""Definds an/the inherited list class MyList."""


class MyList(list):
    """Implement, sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
