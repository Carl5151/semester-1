import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num = int(input("Enter a number: "))

selected = []
# choose given number of names at random 
for x in range(num):
    while True:
        # select random name and store if not already selected
        name = names[random.randint(0, 1000)]
        if name not in selected:
            selected.append(name)
            break

# Display the chosen names, one per line
for name in selected:
    print(name)
