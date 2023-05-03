"""Main module for snake game entitled 'Turtle Terminator'

"""

import snake
import food
import score
import turtle
import time
import random

delay = 0.13
player = snake.SnakeHead()
segments = []

# Main Window
root = turtle.Screen()
root.title("Turtle Terminator")
root.bgcolor("forest green")
root.setup(width=600, height=600)
root.tracer(0)

# Splash screen
def menu():
    welcome = turtle.Turtle()
    welcome.penup()
    welcome.goto(0, -50)
    welcome.write("       WELCOME TO\n" 
            "   TURTLE TERMINATOR!\n\n"
            "  YOU ARE A BABY SNEK!\n"
            "  EAT THE BABY TURTLES\n"
            "     TO GROW STRONK!!!\n"
            "press any key to continue", align="center",
            font=("courier", 28, "bold"))
    welcome.hideturtle()
    root.onkey(welcome.clear, "")    
    main()

def main():
# Main Gameplay
    whole_body = segments
    bebe_turt = food.Food()

    while True:
        root.update()

        # this restricts the player from going directly back from whence they came
        def go_up():
            if player.direction != "down":
                player.direction = "up"
        def go_down():
            if player.direction != "up":
                player.direction = "down"
        def go_left():
            if player.direction != "right":
                player.direction = "left"
        def go_right():
            if player.direction != "left":
                player.direction = "right"

        # Move the end segments first in reverse order
        # inchworm
        # inspired by AceKing
        def move():
            for segment in range(len(segments)-1, 0, -1):
                posx = segments[segment-1].xcor()
                posy = segments[segment-1].ycor()
                segments[segment].goto(posx,posy)

            # Move segments to the head
            if len(segments) > 0:
                posx = player.xcor()
                posy = player.ycor()
                segments[0].goto(posx,posy)
            else:
                segments.clear()

            # Keep the snake moving
            if player.direction == 'up':
                player.sety(player.ycor() + 20)
            elif player.direction == 'down':
                player.sety(player.ycor() - 20)
            elif player.direction == 'left':
                player.setx(player.xcor() - 20)
            elif player.direction == 'right':
                player.setx(player.xcor() + 20)

        root.listen()
        root.onkeypress(go_up, "Up")
        root.onkeypress(go_down, "Down")
        root.onkeypress(go_left, "Left")
        root.onkeypress(go_right, "Right")

        if player.distance(bebe_turt) < 15:
            global delay
            delay -= 0.004
            score.update_score()
            posx = random.randint(-270, 270)
            posy = random.randint(-270, 250)
            bebe_turt.goto(posx, posy)
            time.sleep(0.1)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("darkgreen")
            new_segment.penup()
            segments.append(new_segment)

            for segment in segments:
                segment.goto(1000, 1000)

        # body collision
        for segment in segments:
            if segment.distance(player) < 20:
                # global delay
                time.sleep(1)
                player.goto(0, 0)
                player.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score.clear_score()

        # border collision
        if player.xcor() > 280 or player.xcor() < -280 or player.ycor() > 280 or player.ycor() < -280:
            delay = 0.13
            score.clear_score()
            time.sleep(1)
            player.goto(0, 0)
            for segment in segments:
                segment.goto(1000, 1000)
            whole_body.clear()
            player.direction = "stop"

        move()
        time.sleep(delay)
        # root.mainloop()

if __name__ == "__main__":
    menu()
    root.mainloop()