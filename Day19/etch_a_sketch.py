from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(15)


def backward():
    tim.backward(15)


def left():
    tim.left(10)


def right():
    tim.right(10)


def clear():
    screen.reset()


def main():
    screen.listen()
    screen.onkey(key="w", fun=forward)
    screen.onkey(key="s", fun=backward)
    screen.onkey(key="d", fun=right)
    screen.onkey(key="a", fun=left)
    screen.onkey(key="c", fun=clear)

    screen.exitonclick()


if __name__ == "__main__":
    main()
