# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# set of items contained in both lists
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# displays set of items in both lists without repeats
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add('kiwi')
print(fruit)

# Remove an item from vegetables
vegetables.remove('leek')
print(vegetables)

# Find and display symmetric difference of the two sets
# displays all items unique to each list
sym_dif = fruit.symmetric_difference(vegetables)
print(sym_dif)
