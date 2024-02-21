#!/usr/bin/python3

"""
A class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
"""

class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")