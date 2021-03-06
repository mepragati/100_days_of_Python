from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]


    def create_snake(self):
    #creates snake
        for position in STARTING_POSITION:
            self.add_segment(position)
            

    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)
        new_segment.speed("fastest")

    def extend(self):
        #Read a new segment to the array
        self.add_segment(self.snake_segments[-1].position())


    def move(self):
        #moves snake automatically forward
        for segment_number in range(len(self.snake_segments)-1,0,-1):
            new_x = self.snake_segments[segment_number-1].xcor()
            new_y = self.snake_segments[segment_number-1].ycor()
            self.snake_segments[segment_number].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    
    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

        #Moves defined for Snake
    def right(self):
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)