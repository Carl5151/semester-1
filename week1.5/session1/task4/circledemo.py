# Week 1.5, Session 1: Task 4
import geometry

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
from geometry import Point, Circle


# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
p = Point(3, 4)

#  - Creates a Circle object, using the Point object and a value for radius
circle = Circle(5, p)

#  - Displays the area of the circle
print(circle.area())

#  - Displays the perimeter of the circle
print(circle.perimeter())
