"""
Author: Keertikumar Kubareea
Project: Determine if the year is a leap year

This is how you work out whether if a particular year is a leap year.

* on every year that is divisible by 4 with no remainder

* except every year that is evenly divisible by 100 with no remainder

* unless the year is also divisible by 400 with no remainder

"""


def is_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


y = int(input("Choose a year: "))
if is_leap(year=y):
    print("Leap year")
else:
    print("Not leap year")
