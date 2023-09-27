#!/usr/bin/python3
""" Define Class MagicClass """
import math

class MagicClass:
    """ Class MagicClass """
    def __init__(self, radius=0):
        self.radius = radius

    @property
    def radius(self):
        return (self.__radius)
    
    @radius.setter
    def radius(self, value):
        if (not isinstance(value, int)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        return (math.pi * self.__radius * self.__radius)

    def circumference(self):
        return (2 * math.pi * self.__radius)
