from turtle import Screen, Turtle
from player_paddle import PlayerPaddle


def main():
    # Setting up the screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    # Create and move a paddle
    paddle = PlayerPaddle()

    screen.update()  # Update screen once all the objects have been initialized and move to their respective places
    screen.tracer(1)  # Turn on tracer for the game

    # to move the paddle with keystrokes, get the screen to listen
    screen.listen()
    # when using a function as parameter, do not add parentheses
    screen.onkey(paddle.go_up, "Up")
    screen.onkey(paddle.go_down, "Down")

    screen.exitonclick()


if __name__ == "__main__":
    main()
