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

        self.name = name
        self.dob = dob

    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        Returns a person's intitials
        """
        initials = ''
        for char in range(len(self.name)):
            if char == 0 or self.name[char] == " ":
                initials += self.name[char + 1].upper()

        return initials

    def is_birthday(self):
        """
        Returns Boolean if it's a person's birthday today
        """
        if self.dob == date.today():
            return True
        else:
             return False

    # (see README.md for further details)
