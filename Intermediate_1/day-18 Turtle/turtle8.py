from turtle import Turtle, Screen
from random import randint , choice

# Set up turtle and screen
tim = Turtle()
sc = Screen()

# Turtle appearance
tim.width(2)
tim.speed("fastest")

# Screen background color
sc.bgcolor("black")
#generate a random color using tuplers 
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)



# List of colors
colors = [
    "red", "orange", "yellow"
]

# Function to draw a spirograph
def draw_spirograph(size_of_gap):
    for angle in range(0, 360, size_of_gap):
        tim.pencolor(choice(colors))  # Pick a random color
        tim.circle(100)  # Draw a circle with a radius of 100
        tim.setheading(tim.heading() + size_of_gap)  # Rotate the turtle

# Draw a spirograph with 10 degrees of rotation between each circle
draw_spirograph(5)

# Screen settings
sc.exitonclick()
