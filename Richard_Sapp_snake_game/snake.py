"""SnakeHead object class which represents the player

"""

import turtle

class SnakeHead(turtle.Turtle):
    def __init__(self, shape= "square"):
        super().__init__(shape= shape)
        self.penup()
        self.color("dark green")
        self.speed(0)
        self.goto(0, 0)
        self.direction = "stop"
