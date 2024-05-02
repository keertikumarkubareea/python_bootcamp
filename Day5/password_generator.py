"""
Create a password generator. Input are: number of letters, number of symbols, number of digits
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw = []
for a in range(0, nr_letters):
    pw += [letters[random.randint(0, len(letters) - 1)]]
for n in range(0, nr_numbers):
    pw += [numbers[random.randint(0, len(numbers) - 1)]]
for s in range(0, nr_symbols):
    pw.append(random.choice(symbols))  # same as above

# for loop for shuffling 50 times
for shuffle in range(0, 51):
    first_index = random.randint(0, len(pw) - 1)
    second_index = random.randint(0, len(pw) - 1)
    while first_index == second_index:
        second_index = random.randint(0, len(pw) - 1)
    temp = pw[first_index]
    pw[first_index] = pw[second_index]
    pw[second_index] = temp

# random module comes with a shuffle function. Can completely replace the above by
random.shuffle(pw)

pw_string = ''.join(pw)
print("Your generated password: " + pw_string)
