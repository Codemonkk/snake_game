from turtle import Screen, Turtle
from snake import Snake
import time

#setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

#Moving the Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()






screen.exitonclick()