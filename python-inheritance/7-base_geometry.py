#!/usr/bin/python3
"""
Module 7-base_geometry.py
Defines the BaseGeometry class with area and integer_validator methods.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.
    It includes methods for area calculation and integer validation.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        This method is currently not implemented in the base class.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if 'value' is an integer greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer, with the message
                       "<name> must be an integer".
            ValueError: If 'value' is less than or equal to 0, with the message
                        "<name> must be greater than 0".
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
