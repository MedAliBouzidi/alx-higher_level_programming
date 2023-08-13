#!/usr/bin/pyhton3
def print_matrix_integer(matrix=[[]]):
    trans = []
    for row in matrix:
        trans_row = []
        for i in row:
            trans_row.append(i)
        trans.append(trans_row)
    for row in trans:
        print("{:d}".format(i) for i in row)
