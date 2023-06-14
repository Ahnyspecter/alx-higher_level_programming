#!/usr/bin/python3
# 11-student.py
"""Definds a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.
        Args:
            first_name (str): Represents the first name of the student.
            last_name (str): Represents the last name of the student.
            age (int): Represents he age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets the dictionary representation of the Student."""
        return self.
