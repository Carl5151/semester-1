# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """
        Template to create a Point object
        """
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """
        Returns distance from this Point to Origin
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, new_x, new_y):
        """
        Returns distance from this Point to new Point co-ordinates
        """
        return math.hypot(new_x - self.x, new_y - self.y)

# Add a definition for a Circle class here, giving it
class Circle:
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
    def __init__(self, radius, centre = Point(0.0, 0.0)):
        self.radius = radius
        self. centre = centre

#  - A method area(), returning the area of the circle
    def area(self):
        """
        Returns area of circle
        """
        return math.pi * (self.radius ** 2)
    
#  - A method perimeter(), returning the perimeter of the circle
    def perimeter(self):
            """
            Returns perimeter of circle
            """
            return 2 * math.pi * self.radius * 2

# Don't add any testing code to this file!
