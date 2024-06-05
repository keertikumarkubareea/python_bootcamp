"""
The beginning of OOP
Classes have attributes (what it has) and methods (what it does). Methods are functions that a particular modelled
object can do. They are not free floating functions.

"""
import turtle
from turtle import Turtle, Screen

# tommy - object
# Turtle - class/blueprint
tommy = Turtle()
print(tommy)
# change tommy's shape to an actual turtle using the method
tommy.shape("turtle")
tommy.color("red")

# Drawing a star outline
while True:
    tommy.forward(200)
    tommy.left(170)
    if abs(tommy.pos()) < 1:
        break

my_screen = Screen()
# Accessing an attribute from the object
print(my_screen.canvheight)

# Methods - functions attached to an object
my_screen.exitonclick()  # Instead of a disappearing screen, the program not exits when we click using this method

# For existing libraries, we can get all the available methods and attributes from their documentation on
# docs.python.org and searching for the library
