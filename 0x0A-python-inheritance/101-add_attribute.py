#!/usr/bin/python3
"""Definds a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): Represents the object to add an attribute to.
        att (str): Represents the name of the attribute to add to obj.
        value (any): Represents the value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
