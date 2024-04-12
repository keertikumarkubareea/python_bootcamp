"""
Calculate price of pizza based on size, pepperoni amount and cheese amount.
"""

print("Thank you for choosing Python Pizza Deliveries")
total = 0
size = input("What size of pizza would you like? (S)mall, (M)edium or (L)arge?: ")
p = input("Do you want to add pepperoni? (Y)es or (N)o: ")
if size == "S":
    total += 15
    if p == "Y" or p == "y":
        total += 2
elif p == "Y" or p == "y":
    total += 3
    if size == "M":
        total += 20
    else:
        total += 25
else:
    if size == "M":
        total += 20
    else:
        total += 25

c = input("Add extra cheese? (Y)es or (N)o: ")
if c == "y" or c == "Y":
    total += 1

print(f"Your final bill is ${total}")
