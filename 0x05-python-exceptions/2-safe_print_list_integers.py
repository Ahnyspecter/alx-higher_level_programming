#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are only integers.

    Args:
        my_list (list): The list that elements are printed from.
        x (int): The number of elements of 'my_list' to print.

    Returns:
        The number of elements printed"""

    work = 0
    for m in range(0, x):
        try:
            print("{:d}".format(my_list[m]), end="")
            work += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (work)
