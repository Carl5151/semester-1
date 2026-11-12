# Week 1.7, Session 2: Task 1 - NameError

# Run this program and observe what happens

expenses = [10, 20, 30]

total = 0 # added to prevent crash
for amount in expenses:
    total = total + amount  

print(total)