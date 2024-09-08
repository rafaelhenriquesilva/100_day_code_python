from turtle import Turtle, Screen
import random as r

tim = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", 'SeaGreen' ]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/ num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3,11):
    tim.color(r.choice(colors))
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()