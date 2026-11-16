import random

# Get user to input how many random numbers they want
num = int(input("Enter a number: "))

# Generate this many random numbers
nums = []
for x in range(num):
    nums.append(str(random.randint(0,1000)))

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as f:
    for num in nums:
        f.write(num + "\n")
