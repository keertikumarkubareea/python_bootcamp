"""
Author: Keertikumar Kubareea
Project: BMI calculator
"""


def calc_bmi(weight: float, height: float) -> int:
    bmi = int(weight / (height ** 2))
    return bmi


weight = float(input("What's your weight in kilograms(kg)?: "))
height = float(input("What is your height in metres(m)?: "))
bmi = calc_bmi(weight=weight, height=height)
print("Your BMI is equal to " + str(bmi))
if bmi < 18.5:
    print("You are underweight")
elif bmi < 24.9:
    print("You are healthy")
elif bmi < 29.9:
    print("You are overweight")
else:
    print("You are obese")
