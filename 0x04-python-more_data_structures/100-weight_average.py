#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tap in my_list:
        num += tap[0] * tap[1]
        den += tap[1]

    return (num / den)
