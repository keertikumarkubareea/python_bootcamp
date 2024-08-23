from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.goto(-20, 280)
        self.score = 0
        self.score_turtle.pendown()
        self.score_turtle.write(f"Score = {self.score}", font=("Verdana",
                                                               15, "normal"))

    def update_score(self):
        self.score_turtle.color("black")
        self.score_turtle.write(f"Score = {self.score}", font=("Verdana",
                                                               15, "normal"))
        self.score += 1
        self.score_turtle.color("white")
        self.score_turtle.write(f"Score = {self.score}", font=("Verdana",
                                                               15, "normal"))
