from turtle import Screen
from snake import Snake
import time
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score= ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecting collision with the food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh_food() 
  
    #detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 299 or snake.head.ycor() < -290:
        is_game_on=False
        score.game_over()
        # score.restart()
        # screen.listen()

    #detecting collision with own tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on=False
            score.game_over()

screen.exitonclick()