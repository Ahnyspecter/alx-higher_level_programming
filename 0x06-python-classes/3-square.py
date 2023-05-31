#!/usr/bin/python3
"""Definds the class Square."""


class Square:
    """Represents the square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of the new square."""

        if not isinstance(size, int):
            raise TypeError("size (integer)")
        elif size < 0:
            raise ValueError("size >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)
