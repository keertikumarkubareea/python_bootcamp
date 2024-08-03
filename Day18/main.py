"""
Day 18 - Tutle and the Graphical User Interface
Turtle graphics documentation: https://docs.python.org/3/library/turtle.html
Colors: https://trinket.io/docs/colors
"""

from turtle import Turtle, Screen
import random


def draw_square(turtle: Turtle) -> None:
    # currently turtle is facing east
    for turns in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle: Turtle) -> None:
    for _ in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shapes(turtle: Turtle, colors: list) -> None:
    """Sum of interior angles in a polygon = (n - 2) * 180"""
    color_index = 0
    start_sides = 3
    end_sides = 10
    for sides in range(start_sides, end_sides + 1):
        # change brush color before each shape
        turtle.color(colors[color_index])
        color_index += 1

        interior_angle = ((sides - 2) * 180) / sides
        exterior_angle = 180 - interior_angle

        for _ in range(sides):
            turtle.forward(100)
            turtle.right(exterior_angle)


def walk_randomly(turtle: Turtle) -> None:
    angles = [0, 90, 180, 270]
    turtle.pensize(10)
    for _ in range(200):
        angle = random.choice(angles)
        turtle.setheading(angle)
        color_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.pencolor(color_tuple)
        turtle.forward(25)


def draw_spirograph(turtle: Turtle) -> None:
    turn_total_expected = 360
    turn_angle = 5
    turn_total = int(turn_total_expected / turn_angle)
    for _ in range(turn_total):
        color_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.pencolor(color_tuple)
        turtle.circle(100)
        turtle.left(turn_angle)




def main():
    colors = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "black"]
    screen = Screen()  # the canvas to draw on
    screen.colormode(255)  # set the colormode to 255 to be able to generate random rgb value from 0 to 255

    timmy_the_turtle = Turtle()  # Turtle object with a paint brush on its back to draw
    timmy_the_turtle.shape("turtle")  # change shape of the turtle object
    timmy_the_turtle.color("red")  # change the color of the turtle objects
    timmy_the_turtle.speed("fastest")
    # the above are methods that are defined in the blueprint Turtle class
    # we are calling the methods

    # calling some other methods
    # draw_square(turtle=timmy_the_turtle)
    # draw_dashed_line(turtle=timmy_the_turtle)
    # draw_shapes(turtle=timmy_the_turtle, colors=colors)
    # walk_randomly(turtle=timmy_the_turtle)
    draw_spirograph(turtle=timmy_the_turtle)

    # the canvas/screen disappears once running is done. set it to disappear on click
    screen.exitonclick()


if __name__ == "__main__":
    main()
