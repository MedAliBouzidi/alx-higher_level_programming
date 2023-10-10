#!/usr/bin/python3
""" unction that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    with open(filename, encoding="UTF8") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')

