#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        f_dict = dict(filter(lambda it: it[1] != value, a_dictionary.items()))
        a_dictionary.clear()
        a_dictionary.update(f_dict)
        return a_dictionary
