from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def main():

    # to listen to objects, tell the 'screen' object to listen
    screen.listen()
    # once the screen is listening, we need to bind a function that is triggered when a key is pressed on the keyboard
    # need to use an event listener
    screen.onkey(key="space", fun=move_forward)  # No parentheses with the function name
    # when we pass a function as an argument to another function, there is no parentheses
    # onkey function is known as a higher order function - takes another function as an input and works with it


    screen.exitonclick()


if __name__ == "__main__":
    main()