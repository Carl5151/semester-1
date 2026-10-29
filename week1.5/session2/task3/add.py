# Week 1.5, Session 2: Task 3
from money import Money

# Write a program here that creates two Money objects, prints them,
m1 = Money(10, 99)
m2 = Money(15, 99)
print(m1.__str__())
print(m2.__str__())

# then adds them together and prints their sum
print(m1.__add__(m2))
