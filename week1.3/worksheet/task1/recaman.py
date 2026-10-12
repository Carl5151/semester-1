# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []
ax = 0

for x in range (L):
    if x == 0:
        sequence.append(ax)
    else:
        ax = sequence[x - 1] - x
        if  ax > 0:
            if ax not in sequence:
                sequence.append(ax)
            else:
                sequence.append(sequence[x - 1] + x)
        else:
            sequence.append(sequence[x - 1] + x)


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence