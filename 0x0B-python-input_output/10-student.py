#!/usr/bin/python3
"""
    Define a Class Student
"""


class Student:
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {
                        "first_name": self.first_name,
                        "last_name": self.last_name,
                        "age": self.age
                    }
        res = {}
        for attr in attrs:
            if hasattr(self, attr):
                res[attr] = getattr(self, attr)
        return res
