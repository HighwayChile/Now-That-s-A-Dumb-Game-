"""scoreboard for snek game"""

import turtle

myscore = int()
high_score = int()

class Score():
    def __init__(self, shape= "square", color= "chocolate"):
        super().__init__(self, shape, color)
    self = turtle.Turtle()
    self.speed(0)
    self.penup()
    self.hideturtle()
    self.goto(0, 250)
    self.write(f"Score:{myscore} High Score:{high_score} ", align="center", font=("courier", 27, "bold"))

def update_score():
    global myscore, high_score
    Score.self.clear()
    myscore = myscore + 10
    # high_score = high_score
    if myscore > high_score:
        high_score = myscore
    Score.self.clear()
    Score.self.write(f"Score:{myscore} High Score:{high_score} ", align="center", font=("courier", 27, "bold"))
    return myscore, high_score

def clear_score():
    global myscore, high_score
    # myscore.clear()
    myscore = int()
    high_score = high_score
    Score.self.clear()
    Score.self.write(f"Score:{myscore} High Score:{high_score} ", align="center", font=("courier", 27, "bold"))
