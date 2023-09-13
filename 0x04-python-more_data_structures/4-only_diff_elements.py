#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = {}
    for elem in set_1:
        if elem in set_2 and not elem in new_set:
            new_set.add(elem)
    
    for elem in set_2:
        if elem in set_1 and not elem in new_set:
            new_set.add(elem)
    # return set(filter(lambda x: x not in set_2, set_1)).union(set(filter(lambda x: x not in set_1, set_2)))
    return new_set
