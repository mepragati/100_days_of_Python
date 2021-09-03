from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def move_clockwise():
    tim.right(10)

def move_counterclockwise():
    tim.left(10)

screen.listen()
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(move_counterclockwise,'a')
screen.onkey(move_clockwise,'d')
screen.onkey(clear_screen,'c')

screen.exitonclick()