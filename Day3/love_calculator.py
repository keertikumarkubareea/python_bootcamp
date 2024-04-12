"""
Project: Love score calculator between 2 names
"""

print("Welcome to the love calculator!!")
name1 = input("Please input your name: ")
name2 = input("Please input the name of your love interest: ")

true_count = 0
love_count = 0
for character in name1.lower():
    if character == "t" or character == "r" or character == "u" or character == "e":
        true_count += 1
    if character == "l" or character == "o" or character == "v" or character == "e":
        love_count += 1

for character in name2.lower():
    if character == "t" or character == "r" or character == "u" or character == "e":
        true_count += 1
    if character == "l" or character == "o" or character == "v" or character == "e":
        love_count += 1

score = true_count * 10 + love_count
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}, not so great together")

"""
Alternatively:
Convert to lower case and combine the 2 names into one string. Avoid looping and use the count function as 
follows: combined_names.count("t")
"""
