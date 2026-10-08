# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

print('Enter a sequence of float values')
numbers = read_numbers()

if len(numbers) == 0:
    sys.exit('Error: no numbers provided')
else:
    print('Minimum =', str(min(numbers)))
    print('Maximum =', str(max(numbers)))
    print('Mean =', str(sum(numbers) / len(numbers)))
    numbers.sort()
    if len(numbers) == 1:
        print('Median =', str(numbers[len(numbers)  // 2]))
    else:
        print(f'Median of {numbers} should be', str(numbers[len(numbers)  // 2]))

