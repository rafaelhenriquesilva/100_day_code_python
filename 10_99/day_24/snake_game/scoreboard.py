from turtle import Turtle
import json
from pathlib import Path
ALIGMENT="CENTER"
FONT=('Arial', 20, 'normal')
class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.file_path = Path(__file__).parent / "data.json" 
        self.read_file()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'SCORE: {self.score}, High score: {self.high_score}', align=ALIGMENT, font=FONT)
        

    def reset(self):
        
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def read_file(self):
        try:
            with self.file_path.open("r") as openfile:
                self.json_object = json.load(openfile)
                self.high_score = self.json_object.get("high_score", 0)  
        except (FileNotFoundError, json.JSONDecodeError):  
            self.high_score = 0 

            
    def write_file(self):
        data = {"high_score": self.high_score}
        with self.file_path.open("w") as f:
            json.dump(data, f)  

    