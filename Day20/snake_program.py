"""
Day 20 consists of 3 modules:
1. Building the snake body
2. Moving the snake on the screen
3. Controlling the snake with the keyboard
"""
from snake import Snake
from turtle import Screen
from food import Food
import time


def main():
    # Set up the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)  # turn off tracer, need to call screen.update for any update to happen on the screen
    # this is being done to smoothen the animation of the moving turtle
    # if this is not done, we will see each block in the snake move
    snake = Snake()  # create the snake object
    food = Food()
    screen.update()  # update screen when snake object of 3 turtles has been created
    # completed creating the screen and the snake body
    # moving the snake automatically
    screen.listen()
    game_over = False
    while not game_over:
        screen.update()  # Update once all turtle objects that make up the snake have been moved
        time.sleep(0.1)
        snake.move(pace=20)
        screen.onkey(key="Right", fun=snake.turn_right)
        screen.onkey(key="Left", fun=snake.turn_left)
        screen.onkey(key="Up", fun=snake.go_up)
        screen.onkey(key="Down", fun=snake.go_down)

        # check if the food is being eaten
        if snake.snake_head.xcor() - 20 <= food.food.xcor() <= snake.snake_head.xcor() + 20 and snake.snake_head.ycor() - 20 <= food.food.ycor() <= snake.snake_head.ycor() + 20 :
            food.eaten_by_snake()
            snake.add_block()




    screen.exitonclick()


if __name__ == "__main__":
    main()
