from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
color_list = ["red","green","blue","yellow","orange","purple"]
y_position = [-70,-40,-10,20,50,80]
user_input = screen.textinput("Enter here: ","Who do you think will win the race out of (red/green/blue/yellow/orange/purple)? Enter the colour: ").capitalize()

for turtle_count in range(6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle_count])
    tim.color(color_list[turtle_count])

if user_input:
    is_race_on = True

print(f"You choose: {user_input}")
screen.exitonclick()