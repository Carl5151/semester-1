# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
        if not isinstance(pounds, int) or not isinstance(pence, int):
            raise TypeError("pounds/pence must be integers")
        if pounds < 0:
            raise ValueError("Pounds must be greater than 0")
        if not 0 <= pence < 100:
            raise ValueError("Pence must range from 0-99")
        
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        return "£{:02d}.{:02d}".format(self.pounds, self.pence)

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        if not isinstance(other, Money):
            raise TypeError("other should be a Money object")
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        sum = str(float(self.__str__()[1:]) + float(other.__str__()[1:]))
        return Money(int(sum[:2]), int(sum[3:]))
