#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ Function to read from file """

    with open(filename, 'r', encoding="utf-8") as f:
        date = f.read()
        print(date, end='')
