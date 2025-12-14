#!/usr/bin/python3
"""
Module 7-base_geometry.py
Defines the BaseGeometry class with area and integer_validator methods.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.
    It includes methods for area calculation and robust integer validation.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        This method is not implemented in the base class and serves as an
        interface definition for subclasses.

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
            TypeError: If 'value' is not an integer.
                       Message: "<name> must be an integer".
            ValueError: If 'value' is less than or equal to 0.
                        Message: "<name> must be greater than 0".
        """
        # 1. Type Check: Must be an integer
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # 2. Value Check: Must be greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
