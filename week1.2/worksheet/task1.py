# Worksheet 1.2: Task 1 Solution
import sys

try:
    grade = int(input("Enter an integer grade from 1-100: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if 0 > grade or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
else:
    if grade < 40:
        print(grade, 'is a Fail')
    elif grade < 70:
        print(grade, 'is a Pass')
    else:
        print(grade, 'is a Distinction')
