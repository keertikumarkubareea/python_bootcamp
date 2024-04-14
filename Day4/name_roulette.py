import random

name = input("Insert your guest's name: ")
combined_names = []
while name.lower() != "q":
    combined_names.append(name)
    name = input("Add another guest's name (Type 'Q' or 'q' if you have no other guests): ")

total_guests = len(combined_names)
index = random.randint(0, total_guests - 1)
print(f"{combined_names[index]} is paying for the food!")
