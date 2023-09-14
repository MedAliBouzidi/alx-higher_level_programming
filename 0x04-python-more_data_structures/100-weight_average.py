#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return 0
        sum_wieght = sum([elem[1] for elem in my_list])
        sum_score = sum([elem[0] * elem[1] for elem in my_list])
        return sum_score / sum_wieght
