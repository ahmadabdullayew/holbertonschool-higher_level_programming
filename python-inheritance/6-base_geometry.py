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
    # integer_validator method removed to match the desired output for dir(bg)
    # def integer_validator(self, name, value):
    #     if not isinstance(value, int):
    #         raise TypeError(f"{name} must be an integer")
    #     if value <= 0:
    #         raise ValueError(f"{name} must be greater than 0")
