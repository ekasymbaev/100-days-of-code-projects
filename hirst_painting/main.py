import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
color_list = [(204, 107, 107), (231, 109, 109), (134, 192, 192), (44, 144, 144), (152, 53, 53), (199, 164, 164), (15, 53, 53), (181, 42, 42), (148, 87, 87), (141, 155, 155), (205, 70, 70), (64, 92, 92), (195, 118, 118), (225, 187, 187), (15, 27, 27), (59, 19, 19), (227, 166, 166), (48, 182, 182), (238, 4, 4), (87, 112, 112), (121, 53, 53), (177, 216, 216), (35, 110, 110), (169, 184, 184), (60, 36, 36), (14, 71, 71)]
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):

    tim.dot(20, random.choice(color_list))

    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen = t.Screen()
screen.exitonclick()


