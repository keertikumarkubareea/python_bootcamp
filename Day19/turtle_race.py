"""
Capstone project for Day 19 - The turtle race
"""

from turtle import Turtle, Screen
import random

screen = Screen()


def create_participants(colors: list) -> list:
    participants = []
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        participants.append(turtle)
    return participants


def get_positions(turtles: list) -> list:
    positions = []
    for t in turtles:
        positions.append(t.pos())
    return positions


def main():
    screen.setup(width=500, height=400)
    # ask user to bet which turtle will win
    user_bet = screen.textinput(title="Which turtle will win?",
                                prompt="Red, blue, orange, green, purple or pink?").lower()
    # turtle graphics coordinate system = the origin is at the centre of the screen
    colors = ["red", "blue", "orange", "green", "purple", "pink"]
    participants = create_participants(colors)
    y_coordinate = -150
    x_coordinate = -230  # stays the same
    for p in participants:
        p.penup()
        p.goto(x=x_coordinate, y=y_coordinate)
        y_coordinate += 60

    print(get_positions(turtles=participants))
    race_completed = False
    winner = ""
    while not race_completed:
        for turtle in participants:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= 230:
                race_completed = True
                winner = turtle.pencolor()

    if winner == user_bet:
        print(f"You win! {winner} won the race!!")
    else:
        print(f"You lose! {user_bet} lost the race to {winner}")

    screen.exitonclick()


if __name__ == "__main__":
    main()
