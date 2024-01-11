from turtle import Turtle, Screen
import random

timmy = Turtle()
my_screen = Screen()

colors = ["dark blue", "cyan", "green", "dark slate blue", "deep pink", "maroon", "gold", "lime"]

def draw_shape(n):
    angle = 360/n
    for _ in range(n):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3, 9):
    timmy.color(random.choice(colors))
    draw_shape(sides)

my_screen.exitonclick()