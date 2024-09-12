from turtle import Turtle
ALIGMENT="CENTER"
FONT=('Arial', 20, 'normal')
class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.score}', align=ALIGMENT, font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write('GAME OVER!', align=ALIGMENT, font=FONT)
        
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()