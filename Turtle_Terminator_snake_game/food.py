"""food object class for snek game"""

import turtle
import random

class Food(turtle.Turtle):
    def __init__(self, shape= "turtle"):
        super().__init__(shape)
        positionx= random.randint(-270, 270)
        positiony= random.randint(-270, 250)
        self.shapesize(0.6, 0.6, None)
        self.speed(0)
        self.penup()
        self.goto(positionx, positiony)
        self.color("dark green")
        self.direction = "north"



