#!/usr/bin/python3
"""Module that defines a function to check if two objects are of the same type."""


def is_same_class(obj, a_class):
    """
    Checks if two objects, obj1 and obj2, are exactly the same type.

    Args:
        obj1: The first object.
        obj2: The second object.

    Returns:
        bool: True if obj1 and obj2 have the exact same type, False otherwise.
    """
    return type(obj) is a_class
