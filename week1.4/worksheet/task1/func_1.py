
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
    Takes a list of integers and returns the average of 
    those integers
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 

print(func_1([10, 20, 30, 40, 50, 60]))
