#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for char in my_string:
        if not char in ['c', 'C']:
            new_str += char
    return new_str
