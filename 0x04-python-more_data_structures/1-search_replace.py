#!/usr/bin/python4
def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        return list(map(lambda x: replace if x == search else x, my_list))
