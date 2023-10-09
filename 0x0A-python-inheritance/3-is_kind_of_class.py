#!/usr/bin/python3
""" Define a method to check """


def is_kind_of_class(obj, a_class):
    """
        function that returns True if the object
        is an instance of, or if the object is an instance
        of a class that inherited from, the specified class
        ; otherwise False
        Args:
            obj: to be checked
            a_class: the class
    """

    if isinstance(obj, a_class):
        return True
    return False
