"""
Description: Buyers will bid their prices in secrecy and the highest bidder is revealed at the end
Constraints:
pip install replit
run in terminal
"""
from replit import clear

bidding_logo = '''
                         ___________
                         |         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________|
                       .-------------.
                      /_______________|
'''


def add_buyer(name: str, price: float) -> None:
    buyers[name] = price


print(bidding_logo)
print("------------------------------------------------------------------------")
print("Welcome to the secret bidding")
buyers = {}
buyer = input("Who is the first buyer?: ")
value = float(input(f"What is your bid {buyer}?: $"))
add_buyer(buyer, value)
another = input("Do we have another buyer?: ")
while another.lower() != "no":
    clear()
    buyer = input("Who is the next buyer?: ")
    value = float(input(f"What is your bid {buyer}?: $"))
    add_buyer(buyer, value)
    another = input("Do we have another buyer?: ")

clear()
max_bid = 0
highest_bidder = ""
for key in buyers:
    if buyers[key] > max_bid:
        max_bid = buyers[key]
        highest_bidder = key

if highest_bidder == "":
    print("There is no bid high enough, auction closed!")
else:
    print(f"The highest bidder is {highest_bidder}, with a bidding price of ${max_bid}.")
    print(f"Congratulations {highest_bidder}")
