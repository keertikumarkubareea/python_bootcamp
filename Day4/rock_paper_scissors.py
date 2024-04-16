"""
Capstone project for Day 4: Rock, Paper, Scissors game

"""
import random

game = ["rock", "paper", "scissors"]
player_choice = int(input("1: Rock, 2: Paper, 3: Scissors. Choose a number: "))

while player_choice not in range(4):
    player_choice = int(input("Invalid number!!! 1: Rock, 2: Paper, 3: Scissors. Choose a number: "))

player_choice = game[player_choice - 1]
print(f"You have chosen {player_choice}!!")

print("------------------------------------")

ai_choice = random.randint(0, 2)
ai_choice = game[ai_choice]
print(f"The computer has chosen: {ai_choice}!!")

print("------------------------------------")

if ai_choice == player_choice:
    print("DRAW!")
elif player_choice == "rock":
    if ai_choice == "paper":
        print("The computer wins!!")
    else:
        print("Player wins!!")
elif player_choice == "paper":
    if ai_choice == "scissors":
        print("The computer wins!!")
    else:
        print("Player wins!!")
elif player_choice == "scissors":
    if ai_choice == "rock":
        print("The computer wins!!")
    else:
        print("Player wins!!")




