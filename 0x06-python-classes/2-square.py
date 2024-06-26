#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """In Euclidean geometry, a square is a regular quadrilateral, which means that it has four sides of equal length and four equal angles. 
    It can also be defined as a rectangle with two equal-length adjacent sides"""

    def __init__(self, size=0):
        """Initialize a new Square.
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        