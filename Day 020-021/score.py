from turtle import Turtle
FONT_SCORE = ("Courier",18,"normal")
FONT_GAME_OVER = ("Courier",24,"bold")
FONT_TEXT = ("Courier",14,"normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT_SCORE)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT_GAME_OVER)

    # def restart(self):
    #     self.goto(0,-50)
    #     self.write("Press 'R' to Restart.\nPress 'Esc' to Exit.",align="center",font=FONT_TEXT)