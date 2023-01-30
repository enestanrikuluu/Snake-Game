from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.4)
        self.generate_food()

    def generate_food(self):
        place = (random.randint(-300, 300), random.randint(-300, 300))
        self.goto(place)

    def is_ate(self, other):
        return abs(self.xcor() - other.xcor()) < 14 and abs(self.ycor() - other.ycor()) < 14


