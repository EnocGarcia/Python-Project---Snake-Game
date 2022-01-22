from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

alive = True


def game_over():
    global alive
    alive = False
    scoreboard.game_over()


while alive:
    screen.update()
    sleep(.05)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_pos()
        snake.add_tail()
        scoreboard.add_score()

    # Detect collision with walls
    if(
        snake.head.xcor() >= 300 or
        snake.head.ycor() >= 260 or
        snake.head.xcor() <= -300 or
        snake.head.ycor() <= -300
    ):
        game_over()

    # Detect collisions with the tail
    snake_tail = snake.snake[1:]
    for dot in snake_tail:
        if dot.distance(snake.head) < 10:
            game_over()


screen.exitonclick()
