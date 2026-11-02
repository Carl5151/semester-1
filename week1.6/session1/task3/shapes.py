# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!
class Circle(Shape):
    """
    Subclass of shape for a circle.
    """
    def __init__(self, radius, position, colour='red'):
        super().__init__(position, colour)
        """
        Creates a circle with the specified radius, position & colour.
        """
        self.set_radius(radius)

    def set_radius(self, radius):
        """
        Sets this shape's radius to the given radius.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be an integer or float")
        if radius < 0:
            raise ValueError("Radius must be greater than zero")

        self.radius = radius

    def __str__(self):
        """
        Returns this circle's colour, radius & position.
        """
        return f'{self.colour} circle, radius {self.radius}, at {self.position}'

    def area(self):
        """
        Returns this circle's area.
        """
        return f'{math.pi * (self.radius ** 2):.3f}'

    def perimeter(self):
        """
        Returns this circle's perimeter.
        """
        return f'{2 * math.pi * self.radius:.3f}'
