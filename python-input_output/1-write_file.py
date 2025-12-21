#!/usr/bin/python3
"""
Defines write_file function
"""


def write_file(filename="", text=""):
    """
    Writes a UTF-8 string to a text file and
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
