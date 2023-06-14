#!/usr/bin/python3
# 4-append_write.py
"""Definds a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): Represents the name of the file to append to.
        text (str): Represents he string to append to the file.
    Returns:
        To the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
