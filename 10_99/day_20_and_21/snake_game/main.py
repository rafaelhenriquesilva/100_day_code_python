from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake Game")
# You need to put the image about the old image, to update screen
screen.tracer(0)
list_segment = []
    
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect colision with WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
        
    # Slice is better for this situation
    # Detect colision with TAIL
    # for seg in snake.segments:
    #     if seg == snake.head:
    #         pass
    #     elif(snake.head.distance(seg) < 10):
    #         game_is_on = False
    #         scoreboard.game_over()
    
    for seg in snake.segments[1:]:
        if(snake.head.distance(seg) < 10):
            game_is_on = False
            scoreboard.game_over()
  
        
        

screen.exitonclick()