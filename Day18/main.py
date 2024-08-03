"""
Day 18 - Tutle and the Graphical User Interface
Turtle graphics documentation: https://docs.python.org/3/library/turtle.html
Colors: https://trinket.io/docs/colors
"""

from turtle import Turtle, Screen


def draw_square(turtle: Turtle) -> None:
    # currently turtle is facing east
    for turns in range(4):
        turtle.forward(100)
        turtle.right(90)


def main():
    timmy_the_turtle = Turtle()  # Turtle object with a paint brush on its back to draw
    timmy_the_turtle.shape("turtle")  # change shape of the turtle object
    timmy_the_turtle.color("red")  # change the color of the turtle objects
    # the above are methods that are defined in the blueprint Turtle class
    # we are calling the methods
    # calling some other methods
    draw_square(turtle=timmy_the_turtle)

    screen = Screen()  # the canvas to draw on
    # the canvas/screen disappears once running is done. set it to disappear on click
    screen.exitonclick()


if __name__ == "__main__":
    main()
