"""
Hirst painting project
Colorgram library to extract colors from images -> https://pypi.org/project/colorgram.py/


"""
import colorgram
from turtle import Turtle, Screen
import random


def extract_colors(number_colors: int, image: str) -> list:
    return colorgram.extract(image, number_colors)


def draw_dotted_line(t: Turtle, colors: list) -> None:
    for _ in range(25):
        t.pencolor(random.choice(colors).rgb)
        t.circle(5)
        t.penup()
        t.forward(25)
        t.pendown()


def move_one_row_up(t: Turtle, row_number: int) -> None:
    t.penup()
    t.goto(0, 35 * row_number)
    t.pendown()

def main():
    # configuring turtle and screen
    screen = Screen()
    screen.colormode(255)
    screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

    tim = Turtle()
    tim.speed("fastest")
    tim.pensize(10)
    tim.hideturtle()

    color_palette = extract_colors(number_colors=20, image="hirst_image.jpg")

    for row in range(20):
        move_one_row_up(t=tim, row_number=row)
        draw_dotted_line(t=tim, colors=color_palette)

    screen.exitonclick()


if __name__ == "__main__":
    main()
