#!/usr/bin/python3
"""Module to check instance type"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a_class's subclass"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
