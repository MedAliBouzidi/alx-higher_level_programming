#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set(filter(lambda x: x not in set_2, set_1)).union(set(filter(lambda x: x not in set_1, set_2)))
