# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        try:
            # check if width/height are integer
            if not isinstance(width, int) or  not isinstance(height, int):
                raise TypeError
            # check if width/height are greater than 0
            elif width <= 0 or height <= 0:
                raise ValueError
            else:
                # set attributes if valid arguements passed in
                self.width = width
                self.height = height
        except TypeError:
            print("Invalid width/height data type")
        except ValueError:
            print("Invalid width/height")

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """
        Returns True/False if shape rectangle is a square or not
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        Returns area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns perimeter of rectangle
        """
        return (2 * self.width) + (2 * self.height)

    # (See README.md for details of what they should do)
