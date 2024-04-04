"""
Author: Keertikumar Kubareea
Project: Tip and payment calculator for a bill at a restaurant
"""


def calculate_tip(bill: float, percentage: int) -> float:
    tip = (bill * percentage) / 100
    return tip


def split_total(total: float, head_count: int) -> float:
    return total / head_count


print("Welcome to the tip calculator!")
initial_bill = float(input("What was the total bill?: $"))
tip_percentage = int(input("What percentage of tip would you like to give? (Suggested: 10, 12, or 15): "))
tip_in_dollars = calculate_tip(initial_bill, tip_percentage)
bill_after_tip = initial_bill + tip_in_dollars
persons = int(input("With how many people are you splitting the bill?: "))
final_amount = "{:.2f}".format(round(split_total(bill_after_tip, persons), 2))
print(f"Each person should pay: ${final_amount}")



