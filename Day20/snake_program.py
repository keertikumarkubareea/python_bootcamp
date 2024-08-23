"""
Day 20 consists of 3 modules:
1. Building the snake body
2. Moving the snake on the screen
3. Controlling the snake with the keyboard
"""
from turtle import Screen, Turtle
import time


def create_block() -> Turtle:
    block = Turtle(shape="square")
    block.color("white")
    block.penup()
    return block


def follow_head(snake):
    last_block_index = len(snake) - 1
    # moving the last blocks to the previous-to-last blocks position
    for snake_block in range(last_block_index, 0, -1):  # index 0 is excluded - need to move the head on its own
        new_x = snake[snake_block - 1].xcor()
        new_y = snake[snake_block - 1].ycor()

        snake[snake_block].goto(new_x, new_y)

def main():
    # Set up the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)  # turn off tracer, need to call screen.update for any update to happen on the screen
    # this is being done to smoothen the animation of the moving turtle
    # if this is not done, we will see each block in the snake move

    # create 3 turtles(original length of the snake)
    # shape = square for each turtle
    # one turtle is 20px wide and 20px tall

    # first turtle created at origin(0, 0)
    x_position = 0
    y_position = 0
    snake = []
    # create 3 initial blocks
    for _ in range(3):
        block = create_block()
        block.goto(x_position, y_position)
        x_position -= 20
        snake.append(block)

    screen.update()

    # completed creating the screen and the snake body
    # moving the snake automatically
    snake_head = snake[0]
    game_over = False
    while not game_over:
        screen.update()
        time.sleep(0.1)

        follow_head(snake)
        snake_head.forward(20)

    screen.exitonclick()


if __name__ == "__main__":
    main()
