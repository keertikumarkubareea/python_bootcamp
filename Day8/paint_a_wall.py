"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

Note:
The math.ceil (ceiling) function returns the smallest integer higher or equal to x.

For Python 3:

import math
print(math.ceil(4.2))
For Python 2:

import math
print(int(math.ceil(4.2)))
"""
import math


def paint_calc(height: int, width: int, cover: int) -> None:
    wall_area = height * width
    number_of_cans = math.ceil(wall_area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
