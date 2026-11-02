# Week 1.6, Session 1: Task 3
from point import Point
from shapes import Shape, Circle

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
point = Point(0, 0)
circle = Circle(2.5, point)
print(circle.__str__())
print(circle.area())
print(circle.perimeter())
point = Point(1.6, 3.2)
circle.set_position(point)
print(circle.__str__())
circle.set_colour('green')
print(circle.__str__())
