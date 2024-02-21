#!/usr/bin/python3

"""
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation of the class Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
    def __str__(self):
        """Returns the string representation of the square"""
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))