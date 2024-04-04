"""
Author: Keertikumar Kubareea
Project: Amount of weeks left for a person to live, assuming the person lives till 90
"""


def calc_weeks_left(current_age: int) -> int:
    years_left = 90 - current_age
    months_left = years_left * 12

    # 4.345 is the average number of weeks in a month
    weeks_left = months_left * 4.345
    return round(weeks_left)


age = int(input("What is your current age?: "))
print(f"You have {calc_weeks_left(current_age=age)} weeks left. ")
