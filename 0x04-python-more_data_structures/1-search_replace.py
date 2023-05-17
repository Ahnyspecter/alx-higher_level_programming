#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list(map(lambda p: replace if p == search else p, my_list))
    return (new_list)
