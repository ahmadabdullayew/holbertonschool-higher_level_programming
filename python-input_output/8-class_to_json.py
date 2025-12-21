#!/usr/bin/python3
"""
Defines class_to_json function
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a simple data structure
    for JSON serialization of an object
    """
    return obj.__dict__
