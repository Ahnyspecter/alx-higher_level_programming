#!/usr/bin/python3
def magic_string():
    magic_string.m = getattr(mmagic_string, 'm', 0) + 1
    return ("BestSchool, " * (magic_string.m - 1) + "BestSchool")
