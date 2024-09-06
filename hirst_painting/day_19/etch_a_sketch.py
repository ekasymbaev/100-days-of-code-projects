from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def counter_clockwise():
    tim.left(5)
    tim.forward(10)

def clockwise():
    tim.right(5)
    tim.forward(10)

def clear():
    tim.reset()


screen = Screen()
screen.listen()
#Forwards
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear )



screen.exitonclick()