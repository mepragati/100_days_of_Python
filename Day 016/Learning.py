from turtle import Turtle, Screen
tinny = Turtle()
print(tinny)
tinny.shape("turtle")
tinny.color("coral")
tinny.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()