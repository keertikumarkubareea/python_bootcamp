"""
Author: Keertikumar Kubareea
Project: Can I ride the rollercoaster?

Can only ride if height in cm is at least 120 cm
"""


def can_ride(height: float) -> bool:
    if height >= 120:
        return True
    else:
        return False


h = float(input("Please enter your height (in cm): "))
if can_ride(h):
    print("You can ride the rollercoaster!")
    age = int(input("Please input your age: "))
    if age <= 12:  # Ages between 0 - 12 incl.
        print("Please pay $5.")
    elif age <= 18:  # Ages between 13 - 18 incl.
        print("Please pay $7.")
    else:  # Ages above 18
        print("Please pay $12.")
else:
    print("You need to grow taller before you can ride the rollercoaster")
