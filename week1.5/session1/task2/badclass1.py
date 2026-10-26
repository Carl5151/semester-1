# A bad class implementation

# What does the runtime error mean?
# Error that occurs whilst running the code/ being executed
# How do we fix the code?
# Adding self to the constructor and attributes

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
