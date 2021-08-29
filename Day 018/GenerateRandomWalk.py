import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen","black","dark green","navy","maroon","dark slate blue","purple"]

directions = [0,90,180,270]
# directions = random.randint(0,359)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def random_move():
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

for _ in range(200):
    tim.speed("fastest")
    tim.pensize(10)
    random_move()

t.exitonclick()