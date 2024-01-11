# how to draw a circle
# figure out the size of the circle
# tilt the circle

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(72):
    tim.pencolor(random_color())
    tim.circle(50)
    tim.setheading(tim.heading() + 5)



my_screen = t.Screen()
my_screen.exitonclick()