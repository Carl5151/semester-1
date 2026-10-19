def average(list):
    sum = 0
    for num in list:
        sum += num
    average = sum / len(list)
    return average

integers = []
while True:
    entry = input("Enter an integer or quit to stop: ")
    if entry == 'quit': 
        break
    else:
        try:
            integers.append(int(entry))
        except:
            print("Invalid input")

print(f"Average: {average(integers): .2f}")
