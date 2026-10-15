# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

highest_sale = 0
sum = 0
count = 0
most_sold_widget = ''
most_sold_amount = 0
iteration = 0

# read file
with open("sales.csv", "r") as f:
    # each line
    for line in f:
        if iteration == 0:
            iteration += 1
        else:
            # track sales amount and count
            sum += int(line.split(",")[2])
            count += 1
            # check highest sale amount
            if int(line.split(",")[2]) > highest_sale:
                highest_sale = int(line.split(",")[2])
            # check most sold widget
            if int(line.split(",")[3]) > most_sold_amount:
                most_sold_widget = line.split(",")[1]
                most_sold_amount = int(line.split(",")[3])

average = sum / count

print(f"Highest Sale: £{highest_sale}")
print(f"Average Sale: £{average}")
print(f"Most Sold Widget: {most_sold_widget}")

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows