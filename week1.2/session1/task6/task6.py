# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    'Yena': ['Love War', 'HATE XX', 'GOOD MORNING'],
    'DAY6': ['DAYDREAM', 'SUNRISE', 'MOONRISE']
}

# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
print(music['Yena'][1])
print(music['Yena'])
for key in music:
    print(music[key])

