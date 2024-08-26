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

    def add_block(self):
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.penup()
        last_block = self.snake[-1]
        heading_last_block = int(last_block.heading())
        if heading_last_block == 0:  # going east
            new_block.goto(last_block.xcor() - 20, last_block.ycor())
        elif heading_last_block == 90:  # going north
            new_block.goto(last_block.xcor(), last_block.ycor() - 20)
        elif heading_last_block == 180:  # going west
            new_block.goto(last_block.xcor() + 20, last_block.ycor())
        else:  # going south
            new_block.goto(last_block.xcor(), last_block.ycor() + 20)
        self.snake.append(new_block)

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

    def delete_snake(self):
        for block in self.snake:
            block.hideturtle()

    def snake_bites_itself(self) -> bool:
        # TODO: Fix this method
        for snake_body in range(1, len(self.snake)):
            x_cor_max = self.snake[snake_body].xcor() + 10
            x_cor_min = self.snake[snake_body].xcor() - 10
            y_cor_max = self.snake[snake_body].ycor() + 10
            y_cor_min = self.snake[snake_body].ycor() - 10
            if x_cor_max >= self.snake_head.xcor() >= x_cor_min:
                if y_cor_max >= self.snake_head.xcor() >= y_cor_min:
                    return True
        return False

    def snake_collides_with_walls(self) -> bool:
        if self.snake_head.xcor() >= 300 or self.snake_head.xcor() <= -300:
            return True
        elif self.snake_head.ycor() >= 300 or self.snake_head.ycor() <= -300:
            return True
        else:
            return False
