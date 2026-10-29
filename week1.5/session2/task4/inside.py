# Week 1.5, Session 2: Task 4
from geometry import Circle, Point

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
point = Point(1.0, 1.5)
circle = Circle(0.5)

if point in circle:
    print("point is inside circle!")
else:
    print("point is not inside circle!")