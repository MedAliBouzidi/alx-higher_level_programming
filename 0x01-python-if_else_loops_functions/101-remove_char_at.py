#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    for i, c in enumerate(str):
        if not i == n:
            new_str += c
    return new_str
