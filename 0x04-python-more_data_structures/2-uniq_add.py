#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = {}
    for num in my_list:
        uniq[num] = 0
    return sum(uniq.keys())
