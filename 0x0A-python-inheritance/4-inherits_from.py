#!/usr/bin/python3
#AhnySlippe
"""Definds an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an/the object(s) is an inherited instance of a class.

    Args:
        obj (any): Represents the object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
