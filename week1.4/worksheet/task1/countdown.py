import time

def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    print(number)
    time.sleep(1)
    if number != 0:
        countdown(number-1)

num = int(input("Enter an integer: "))
countdown(num)
