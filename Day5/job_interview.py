"""
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the
FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
"""
for num in range(1, 101):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
