#!/usr/bin/python3
"""Definds the class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): The size of the new square"""

        self.size = size

    @property
    def size(self):

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size (integer)")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
