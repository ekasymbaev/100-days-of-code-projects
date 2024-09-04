import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
t.colormode(255)
for i in range(0, 361, 3):
    tim.circle(150)
    tim.setheading(i)
    tim.color(random_color())




screen = t.Screen()
screen.exitonclick()
