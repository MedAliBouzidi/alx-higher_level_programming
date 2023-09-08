#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for row in matrix:
            print(" ".join("{:d}".format(i) for i in row))
