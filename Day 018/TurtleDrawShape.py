import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
########### Challenge 3 - Draw Shapes ########
def angle(sides):
  return 360/sides

def draw(sides):
  tim.forward(100)
  tim.right(angle(sides))

for num_sides in range(3,11):
    tim.color(random.choice(colours))
    for i in range(num_sides):
        draw(num_sides)


t.exitonclick()