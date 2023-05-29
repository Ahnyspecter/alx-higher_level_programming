#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the result when a &  b are divided."""
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
