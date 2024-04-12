"""
Author: Keertikumar Kubareea
Project: Day 3: Treasure hunt game

Link to ASCII arts: https://ascii.co.uk/art

"""
print("Welcome to Treasure Island.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____

*******************************************************************************''')

print("Your mission is to find the treasure")
direction = input("You're at a cross road. Where do you want to go? \"left\" or \"right\"?: ")

while direction != "left" and direction != "right":
    direction = input(f"Direction \"{direction}\" is not a viable option, \"left\" or \"right\"?: ")

if direction == "right":
    print("You fell into a hole. Game over.")
else:
    river_action = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait "
                         "for a boat. Type \"swim\" to swim across: ")
    while river_action != "wait" and river_action != "swim":
        river_action = input(f"Wrong \"{river_action}\" action; \"swim\" or \"wait\" for a boat?: ")

    if river_action == "swim":
        print("You have been attacked and killed by sharks. Game over.")
    else:
        room = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                     "blue. Which colour do you choose?: ")
        while room != "red" and room != "blue" and room != "yellow":
            room = input(f"Wrong \"{room}\" room. Choose either blue, yellow or the red room: ")

        if room == "red":
            print("You enter a room full of fire. So close! Game over.")
        elif room == "blue":
            print("You enter a room of beasts. You were so close! Game over.")
        else:
            print("In the yellow room, you dig the spot marked X. You found the treasure! You win!")
