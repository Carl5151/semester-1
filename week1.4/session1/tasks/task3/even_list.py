def even_integers(num):
    """Returns list of even numbers from 0 up to the input number"""
    evens = []
    for x in range(num + 1):
        if x % 2 == 0:
            evens.append(x)
    return evens

num = int(input("Enter an integer: "))
print(even_integers(num))
