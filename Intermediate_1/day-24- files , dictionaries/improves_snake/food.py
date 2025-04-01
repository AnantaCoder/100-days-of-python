from turtle import Turtle
from random import randint

class Food(Turtle):  # Inherit from Turtle class
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")  # Set the shape of the food
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make it smaller
        self.color('white')  # Color of the food
        self.speed("fastest")  # Make it appear instantly at new locations
        self.refresh()

    def refresh(self):
        # Move the food to a random location within the screen bounds
        rand_x = randint(-270, 270)
        rand_y = randint(-270, 270)
        self.goto(rand_x, rand_y)
