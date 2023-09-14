#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        filtered_dict = dict(filter(lambda item: item[1] != value, a_dictionary.items()))
        a_dictionary.clear()
        a_dictionary.update(filtered_dict)
        return a_dictionary
