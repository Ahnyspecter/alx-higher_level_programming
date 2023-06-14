#!/usr/bin/python3
# 0-read_file.py
"""Definds the text file-reading function."""


def read_file(filename=""):
    """Prints the content(s) of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
