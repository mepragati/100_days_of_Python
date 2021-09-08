from turtle import Turtle

FONT = ("Courier", 18, "normal")
FONT_GAMEOVER = ("Courier", 24, "bold")
ALIGNMENT = "center" 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level=0
        self.goto(-220,260)
        self.update_score()
    
    def update_score(self):
        self.write(f"Level: {self.level}",align=ALIGNMENT,font=FONT)

    def increase_level(self):
        self.level+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font= FONT_GAMEOVER)