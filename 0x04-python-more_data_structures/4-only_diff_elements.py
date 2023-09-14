#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set_1 = set(filter(lambda x: x not in set_2, set_1))
    new_set_2 = set(filter(lambda x: x not in set_1, set_2))
    return new_set_1.union(new_set_2)
