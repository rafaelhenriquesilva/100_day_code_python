from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_fowards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
     new_heading = tim.heading() - 10
     tim.setheading(new_heading)
     
def clear():
    tim.clear()



# Listen the keyboard
screen.listen()
# Event Key
screen.onkey(key='w', fun=move_fowards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)


screen.mainloop()