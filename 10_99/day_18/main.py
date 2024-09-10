# * - Import Everthing
# Desorganized with many module
# alias - import turtle as t
# Instaling modules 
#   https://pypi.org/
# example: pip install heroes

from turtle import Turtle, Screen
import heroes

def runLine(turtle: Turtle):
    turtle.forward(100)
    turtle.right(90)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')

for _ in range(4):
    runLine(timmy_the_turtle)
    
print(heroes.gen())


screen = Screen()
screen.exitonclick()