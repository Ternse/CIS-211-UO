'''
CIS 211

Author: Ernest Ho

Credits: the GitHub book

A mini project to test our knowledge of Classes, and ensure that this file
passes the given tests.

Note - I was given an extension

'''
#File: point.py


class Point:
    def __init__(self, x: int, y: int):             # This is the constructor for Point
        """Assign (self.x = x, self.y = y)"""
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """Move to (x+dx, y+dy)"""
        self.x += dx
        self.y += dy

    def __eq__(self, other: 'Point') -> bool:
        """assertEqual self.x to other.x and self.y to other.y"""
        if self.x == other.x and self.y == other.y:
            return True
        else:
            False
            return False

    def __str__(self):                               # Format str to properly print a Point object.
        """Return f'({self.x}, {self.y})' """
        return f'({self.x}, {self.y})'