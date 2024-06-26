#!/usr/bin/python3
# 0-square.py
"""Define a class Square. """


class Square:
    """Represent a square.
    In Euclidean geometry, a square is a regular quadrilateral, which means that it has four sides of equal length and four equal angles. 
    It can also be defined as a rectangle with two equal-length adjacent sides"""
   
    def __init__(self, size):
        """Initialize a new Square.
            size (int): The size of the new square.
        """
        self.__size = size
