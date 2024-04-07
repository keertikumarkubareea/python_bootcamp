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
    price = 0
    if age <= 12:  # Ages between 0 - 12 incl.
        print("Child tickets are $5.")
        price = 5
    elif age <= 18:  # Ages between 13 - 18 incl.
        print("Youth tickets are $7.")
        price = 7
    else:  # Ages above 18
        print("Adult tickets are $12.")
        price = 12
    pics = input("Do you want photos? (y or n): ")
    if pics == "y" or pics == "Y":
        price += 3
    print (f"Your total payment due is ${price}")
else:
    print("You need to grow taller before you can ride the rollercoaster")
