#!/usr/bin/python3
"""
Defines a Student class with attribute filtering
"""


class Student:
    """
    Represents a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, returns only those attributes.
        Otherwise returns all attributes.
        """
        if isinstance(attrs, list):
            filtered = {}
            for attr in attrs:
                if attr in self.__dict__:
                    filtered[attr] = self.__dict__[attr]
            return filtered

        return self.__dict__
