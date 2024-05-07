"""
Checking if an input is a prime number
Prime numbers are ONLY divisible by 1 and by themselves
"""


def prime_checker(number: int) -> None:
    is_prime = True
    count = 1
    while is_prime and count < 101:
        if count != 1 and count != number:
            if number % count == 0:
                is_prime = False
        count += 1
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


n = int(input("Please enter a prime number: "))  # Check this number
prime_checker(number=n)
