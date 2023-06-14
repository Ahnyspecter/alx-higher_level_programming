"""Definds a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns to the dictionary represntation of a simple data structure."""
    return obj.__dict__
