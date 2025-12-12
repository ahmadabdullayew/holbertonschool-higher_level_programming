#!/usr/bin/python3
"""This module defines a Rectangle class.
"""


class Rectangle:
    """Represent a rectangle."""
    count = 0  # Class attribute to track number of instances
    print_symbol = "#" # Symbol used for string representation
    def __init__(self, width=0, height=0):
        # Use the property setters to set initial values,
        # which will perform validation
        self.width = width
        self.height = height
        Rectangle.count += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area.
        
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        
        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        
        Returns:
            Rectangle: The rectangle with the greater area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
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
        """Return the string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append(Rectangle.print_symbol * self.width)
        return "\n".join(lines)
    
    def __repr__(self):
        """Return a string representation that can recreate the rectangle."""
        return f"{Rectangle.count} instances of Rectangle"

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.count -= 1
