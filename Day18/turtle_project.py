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
    for _ in range(10):
        t.pencolor(random.choice(colors).rgb)
        t.circle(5)
        t.penup()
        t.forward(25)
        t.pendown()


def main():
    # configuring turtle and screen
    tim = Turtle()
    tim.speed("fastest")
    tim.pensize(10)

    screen = Screen()
    screen.colormode(255)

    color_palette = extract_colors(number_colors=10, image="hirst_image.jpg")
    draw_dotted_line(t=tim, colors=color_palette)

    screen.exitonclick()


if __name__ == "__main__":
    main()
