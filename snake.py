from turtle import Turtle

destination = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]

UP = 90
DOWN = 270
RIGHT = 360
LEFT = 180


class Snake:

    def __init__(self):
        self.segment = []
        self.create()
        self.head = self.segment[0]

    def create(self):
        for position in destination:
            self.add_segment(position)

    def add_segment(self, position):
        zoro = Turtle(shape="square")
        zoro.color("white")
        zoro.penup()
        zoro.goto(position)
        self.segment.append(zoro)

    def extent(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(10)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create()
        self.head = self.segment[0]

    def up(self):
        if self.head != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head != RIGHT:
            self.head.setheading(LEFT)
