from turtle import Turtle, Screen
from random import choice


erzho = Turtle()
erzho.shape("turtle")
erzho.color("red")
erzho.speed(60)
erzho.pensize(3)
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Cyan", "Pink", "Brown", "Magenta"]

n = 3

while n<11:
    for i in range(n):
        erzho.forward(100)
        erzho.right(360/n)
    erzho.color(choice(colors))
    n+=1












screen = Screen()
screen.exitonclick()
