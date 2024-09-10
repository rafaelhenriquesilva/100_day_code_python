MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle 
class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        position = 0
        for _ in range(0, 3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(position, 0)
            position -= MOVE_DISTANCE
            self.segments.append(segment)
            
    def move(self):
        # Pieces of snake need to walk together, this form is essential to it
        for seg_num in range((len(self.segments) - 1), 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.setHead(UP)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.setHead(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.setHead(LEFT)
        
    def down(self):
        if self.head.heading() != UP:
            self.setHead(DOWN)
        
        
    def setHead(self, value):
        self.head.setheading(value)