#!/usr/bin/python3
# 3-write_file.py
"""Definds a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): Represents the name of the file to write.
        text (str): Represents the text to write to the file.
    Returns:
        To the number of character(s) written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
