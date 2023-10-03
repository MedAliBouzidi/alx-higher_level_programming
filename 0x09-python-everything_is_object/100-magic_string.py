#!/usr/bin/python3
def magic_string():
    magic_string.occ = getattr(magic_string, 'occ', 0) + 1
    return (f"{'BestSchool, ' * (magic_string.occ - 1)} BestSchool")
