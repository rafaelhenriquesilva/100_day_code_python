import turtle as t
import random as random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

tuples = (1,3,8)
directions = [0,90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_result = (r,g,b)
    
    return random_color_result

tim.pensize(15)
tim.speed('fastest')
for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen.exitonclick()