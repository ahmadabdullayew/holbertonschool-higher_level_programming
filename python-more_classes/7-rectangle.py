#!/usr/bin/python3
"""
This module defines a Rectangle class with properties for width and height,
class attributes for instance counting and representation symbol, and
methods for area, perimeter, string representation, and deletion.
"""


class Rectangle:
    """
    Represent a rectangle, tracking instance count and using a 
    configurable symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance, incrementing the instance count.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable string representation using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        lines = [
            str(self.print_symbol) * self.width
            for _ in range(self.height)
        ]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string that can recreate the instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message and decrement instance counter when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
