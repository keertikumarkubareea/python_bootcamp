"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first
 even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not
every step of the calculation.

"""

target = int(input("Enter a number between 0 and 1000: "))
sum_even = 0
for num in range(0, target + 1, 2):
    sum_even += num

print(f"Sum of even numbers between 0 and {target} = {sum_even}")


