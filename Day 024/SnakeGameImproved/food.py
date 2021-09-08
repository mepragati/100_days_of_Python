from turtle import Turtle
import random

food_colors = ["red","blue","green","purple","yellow","orange"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.color(random.choice(food_colors))
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x,random_y)
