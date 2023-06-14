#!/usr/bin/python3
# 6-from_json_string.py
"""Definds a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns to the Python object representation of a JSON string."""
    return json.loads(my_str)
