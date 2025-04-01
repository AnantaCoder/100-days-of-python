from turtle import Turtle, Screen
from random import choice

# Set up turtle and screen
tim = Turtle()
sc = Screen()

# Turtle appearance
tim.shape("turtle")
tim.color("gold")
tim.width(5)
tim.speed(22)

# Screen background color
sc.bgcolor("black")

# List of colors for rainbow effect
colors = [
    "red", "orange", "yellow", "green", "blue", "indigo", "violet"
]

# Turtle drawing loop random 
deg = [0,90,180,270]
#creating a random maze 

for _ in range(10000000000000000000000000000):
    tim.forward(50)
    tim.left(choice(deg))
    tim.color(choice(colors))
   


# Screen settings
sc.exitonclick()
