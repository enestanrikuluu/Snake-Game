from turtle import *
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.turtles = []

        for i in range(3):
            new_turtle = Turtle()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.goto(-20 * i, 0)
            self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            position = (self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor())
            self.turtles[i].goto(position)

        def up():
            if self.turtles[0].heading() != 270:
                self.turtles[0].setheading(90)

        def down():
            if self.turtles[0].heading() != 90:
                self.turtles[0].setheading(270)

        def left():
            if self.turtles[0].heading() != 0:
                self.turtles[0].setheading(180)

        def right():
            if self.turtles[0].heading() != 180:
                self.turtles[0].setheading(0)

        self.turtles[0].forward(20)
        listen()
        onkey(up, 'Up')
        onkey(down, 'Down')
        onkey(left, 'Left')
        onkey(right, 'Right')

    def game_over_check(self):
        if abs(self.turtles[0].xcor()) >= 310 or abs(self.turtles[0].ycor()) >= 320:
            self.write_game_over()
            return True
        for i in range(1, len(self.turtles)):
            if abs(self.turtles[0].xcor() - self.turtles[i].xcor()) <= 5 and abs(self.turtles[0].ycor() - self.turtles[i].ycor()) <= 5:
                self.write_game_over()
                return True

    def write_game_over(self):
        self.turtles[0].goto(0, 0)
        self.turtles[0].write("Game over.", align="center", font=('Arial', 20, 'bold'))

    def add_segment(self):
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(self.turtles[len(self.turtles)-1].pos())
        self.turtles.append(new_turtle)

