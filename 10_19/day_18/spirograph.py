import turtle as t
import random as random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_result = (r,g,b)
    
    return random_color_result

def createCicle(tim, size):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + size)
    
def draw_spirograph(size):
    for _ in range(int(360 / size)):
        createCicle(tim, size)
    

tim.speed('fastest')
draw_spirograph(5)

screen.exitonclick()