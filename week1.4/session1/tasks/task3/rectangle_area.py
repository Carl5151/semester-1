
# function implementation

def rectangle_area(width, height):  # define suitable input data
    area = width * height              # implement the function
    return area            # return an appropriate value

# testing the function
width = int(input("Enter width: "))
height = int(input("Enter height: "))

print(f"Area is {rectangle_area(width, height)}")   # provide suitable data matching your inputs
