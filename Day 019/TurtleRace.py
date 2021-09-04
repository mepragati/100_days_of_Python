from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
screen = Screen()
screen.setup(width=500,height=400)
color_list = ["red","green","blue","yellow","orange","purple"]
y_position = [-70,-40,-10,20,50,80]
user_input = screen.textinput("Enter here: ","Who do you think will win the race out of (red/green/blue/yellow/orange/purple)? Enter the colour: ").capitalize()

for turtle_count in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_count])
    new_turtle.color(color_list[turtle_count])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_input.lower():
                print(f"You won.The {winning_color.capitalize()} turtle is the winner!")
            else:
                print(f"You lost.The {winning_color.capitalize()} turtle is the winner and you chose {user_input}!")
            
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()