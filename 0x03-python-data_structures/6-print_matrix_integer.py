#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for row in matrix:
            for cell in row:
                print("{:d}".format(cell), end=" ")
            print(end="\n")
