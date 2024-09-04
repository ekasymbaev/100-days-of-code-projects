import turtle as t
import random


erzho = t.Turtle()
erzho.shape("turtle")
erzho.color("red")
erzho.speed(90)
erzho.pensize(10)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]

for _ in range(1000):
    erzho.color(random_color())
    erzho.setheading(random.choice(directions))
    erzho.forward(30)















screen = t.Screen()
screen.exitonclick()
