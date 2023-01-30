from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
food.generate_food()
is_eaten = False
score_board = ScoreBoard()
score_board.update_score_board()
is_game_over = False
while not is_game_over:
    if is_eaten:
        score_board.update_score()
        food.generate_food()
        snake.add_segment()
        is_eaten = False
    screen.update()
    time.sleep(0.1)
    snake.move()
    is_eaten = food.is_ate(snake.turtles[0])
    is_game_over = snake.game_over_check()
screen.exitonclick()
