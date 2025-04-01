'''
*   CREATE  A SNAKE BODY 
*    MOVE THE SNAKE 
*    CONTROL THE SNAKE 
*   DETECT COLLISION WITH FOOD 
*    CREATE A SCOREBOARD 
*   DETECT COLLISION WITH THE WALL 
*   DETECT COLLISION WITH THE WALL 
'''

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Game window setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lime green")
screen.title("Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the scoreboard
scoreboard.start_scoreboard()

game_is_on = True

# Function to restart the game
def restart_game(x, y):
    global game_is_on
    game_is_on = True
    snake.reset()  # Reset the snake to its original state
    scoreboard.reset()  # Reset the scoreboard
    screen.onclick(None)  # Disable further clicks until next game over
    game_loop()  # Restart the game loop

# Main game loop
def game_loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.increase_scoreboard()
            snake.extend()
            food.refresh()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()
            screen.title("Game Over! Click anywhere to restart.")
            screen.onclick(restart_game)

        # Detect collision with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                screen.title("Game Over! Click anywhere to restart.")
                screen.onclick(restart_game)

# Start the game
game_loop()

# Keep the screen open
screen.mainloop()
