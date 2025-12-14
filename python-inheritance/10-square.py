#!/usr/bin/python3
"""Module to check instance type"""

Rectangle = __import__('9-rectangle.py').Rectangle


def square(size):
    """Create a square instance of Rectangle"""
    return Rectangle(size, size)
