from dice import Die
from statistics import stdev
import random, matplotlib.pyplot as plt

die = Die(10) # creates 10 sided die
rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # store roll count of each side

# roll die 100 times
for x in range(100):
    # keep track of each roll
    roll = random.randint(1, 10)
    rolls[roll - 1] += 1

# plotting bar graph of rolls
# creating x axis
x = list(range(1, 11)) # creates list of numbers 1-10

plt.bar(x, rolls) # creating bar chart

# labeling axis
plt.xlabel('Side Rolled')
plt.ylabel('Occurences')

plt.show() # display bar chart

