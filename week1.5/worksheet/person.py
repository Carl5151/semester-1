# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, dob):
        try:
            # check if name is a string
            if not isinstance(name, str):
                raise TypeError
            # check if name is an empty string
            if name == '':
                raise ValueError
            # check if date of birth is a date
            elif not isinstance(dob, date):
                raise TypeError
        except TypeError:
            print("Invalid name/dob data type")
        except ValueError:
            print("No name given")

    # Implement methods initials() and is_birthday() here
    

    # (see README.md for further details)
