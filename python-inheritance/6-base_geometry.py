#!/usr/bin/python3
"""Module to check instance type"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """
        Calculates the area.
        Raises an Exception indicating the method is not implemented.
        """
        raise Exception("area() is not implemented")
