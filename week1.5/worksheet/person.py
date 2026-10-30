# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person object with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, dob):
        """
        Creates a Person, given values for name and date of birth.
        """
        # check if name is a string
        if not isinstance(name, str):
            raise TypeError("Invalid name data type")
        # check if name is an empty string
        if name == '':
            raise ValueError("Name cannot be an empty string")
        # check if date of birth is a date
        if not isinstance(dob, date):
            raise TypeError("Invalid dob data type")

        self.name = name
        self.birth = dob

    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        Returns a person's intitials
        """
        initials = self.name[0].upper()
        for char in range(len(self.name)):
            if self.name[char] == " ":
                initials += self.name[char + 1].upper()

        return initials

    def is_birthday(self):
        """
        Returns Boolean if it's a person's birthday today
        """
        if self.birth == date.today():
            return True
        else:
             return False

    # (see README.md for further details)

# person = Person('Carl Guevan', date(2026, 10, 30))
# print(date.today())
# print(person.is_birthday())