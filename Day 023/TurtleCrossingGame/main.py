import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    #detecting collision with the top edge
    if player.is_at_finish():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

    #detecting collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()