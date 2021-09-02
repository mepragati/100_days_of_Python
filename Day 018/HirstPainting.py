# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day 018\image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle
import random

def draw_dot(color):
    tim.dot(20,color)
    tim.penup()
    tim.forward(50)

def change_direction(i):
    if i%2 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)


turtle.colormode(255)
colors_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = turtle.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for _ in range(10):
        color = random.choice(colors_list)
        draw_dot(color)
    change_direction(i)
    tim.forward(50)

screen = turtle.Screen()
screen.exitonclick()