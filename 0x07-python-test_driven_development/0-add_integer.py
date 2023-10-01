#!usr/bin/python3
""" Add Integers """
def add_integer(a, b=98):
    """
    Function for adding two numbers

    Args:
        a: first number
        b: second number

    Returns:
        The sum of a and b
    
    Raises:
        TypeError: If a or b aren't intege rand/or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))