"""
Guessing the number game with 2 difficulty levels: Easy (10 attempts), hard (5 attempts)
"""
import random


def generate_number() -> int:
    random_number = random.randint(1, 100)
    return random_number


def decrement_attempts(number_of_attempts:int) -> int:
    return number_of_attempts - 1


def main():
    print("Welcome to the number guessing game!!")
    number = generate_number()
    print("I am thinking of a number from 1 to 100 . . .")
    print(f"Psst...the number is {number}")
    difficulty = "".lower()
    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("Please choose a valid difficulty: 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    number_found = False
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            attempts = 0
            number_found = True
            continue

        print("Guess again")
        attempts = decrement_attempts(attempts)

    if number_found:
        print(f"You got it! The number was {number}.")
    else:
        print("Oops. You've run out of guesses. You lose.")


if __name__ == "__main__":
    main()
