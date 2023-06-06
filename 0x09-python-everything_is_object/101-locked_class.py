#!/usr/bin/python3
"""Definds the LockedClass"""

class LockedClass:
    """
    Prevents the user from instanting new LockedClass attributes from
    anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
