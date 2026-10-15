# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
file_name = input("Enter file name: ")

# open and read the file
# word_count = 0
# with open(f"week1.3/session2/task2/1_word_counter/{file_name}", "r") as file:
#     # iterates through each line in file
#     for line in file:
#         # ensures gaps in file not included
#         if line != '\n':
#             # creates list of all words on line without spaces
#             words = line.strip().split(" ")
#             # counts words
#             for word in range(len(words)):
#                 word_count += 1

# second method
with open(f"{file_name}", "r") as file:
    data = file.read()
    data = data.strip().split()
    word_count_2 = len(data)

print(word_count_2)

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount
# print(word_count)

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210