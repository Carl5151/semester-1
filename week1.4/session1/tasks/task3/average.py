def average(list):
    """Returns the average of list"""
    sum = 0
    for num in list:
        sum += num
    average = sum / len(list)
    return average

integers = []
# Appends integers to list till said to stop
while True:
    entry = input("Enter an integer or quit to stop: ")
    if entry == 'quit': 
        break
    else:
        try:
            integers.append(int(entry))
        except:
            print("Invalid input")

# Outputs the average
print(f"Average: {average(integers): .2f}")
