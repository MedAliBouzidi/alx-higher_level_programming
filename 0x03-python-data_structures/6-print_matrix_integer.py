#!/usr/bin/pyhton3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            print("{:d}".format(cell), end=" ")
        print(end="\n")
