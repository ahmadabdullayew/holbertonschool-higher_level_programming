#!/usr/bin/python3
"""
Defines a Student class with JSON serialization/deserialization
"""


class Student:
    """
    Represents a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance
        """
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
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        from a dictionary json.
        """
        for key, value in json.items():
            setattr(self, key, value)
