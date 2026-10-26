# Week 1.5, Session 1: Task 3
import math

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

# Finally, add code here to demonstrate use of Point
p = Point(3, 4)
print(p.distance())
print(p.distance_to(10, 15))
