from turtle import Turtle


class Snake:

    def __init__(self):
        """
        Creating the snake with 3 initial blocks
        """
        def create_block() -> Turtle:
            b = Turtle(shape="square")
            b.color("white")
            b.penup()
            return b

        # create 3 turtles(original length of the snake)
        # shape = square for each turtle
        # one turtle is 20px wide and 20px tall

        # first turtle created at origin(0, 0)
        x_position = 0
        y_position = 0
        self.snake = []
        # create 3 initial blocks
        for _ in range(3):
            block = create_block()
            block.goto(x_position, y_position)
            x_position -= 20
            self.snake.append(block)
        self.snake_head = self.snake[0]

    def follow_head(self):
        last_block_index = len(self.snake) - 1
        # moving the last blocks to the previous-to-last blocks position
        for snake_block in range(last_block_index, 0, -1):  # index 0 is excluded - need to move the head on its own
            new_x = self.snake[snake_block - 1].xcor()
            new_y = self.snake[snake_block - 1].ycor()

            self.snake[snake_block].goto(new_x, new_y)

    def move(self, pace):
        self.follow_head()
        self.snake_head.forward(pace)

    def turn_right(self):
        if int(self.snake_head.heading()) != 180:
            self.snake_head.setheading(0)

    def turn_left(self):
        if int(self.snake_head.heading()) != 0:
            self.snake_head.setheading(180)

    def go_up(self):
        if int(self.snake_head.heading()) != 270:
            self.snake_head.setheading(90)

    def go_down(self):
        if int(self.snake_head.heading()) != 90:
            self.snake_head.setheading(270)
