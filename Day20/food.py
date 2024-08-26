from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.color("blue")
        self.food.shapesize(0.5)
        self.food.penup()
        self.food.goto(random.randint(-280, 280), random.randint(-280, 270))

    def eaten_by_snake(self):
        self.food.goto(random.randint(-280, 280), random.randint(-280, 270))

    def game_over(self):
        self.food.hideturtle()
