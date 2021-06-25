from turtle import Turtle, Screen

# initialize the classes
turtle = Turtle()
screen = Screen()


# to control the turtle's distance as they move forwards
def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def move_counter_clockwise():
    turtle.left(10)


def move_clockwise():
    turtle.right(10)


def clear_drawing():
    turtle.reset()


# offset the event listeners
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=move_counter_clockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
