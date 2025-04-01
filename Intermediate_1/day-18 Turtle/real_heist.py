import turtle as t 


# to generate a random rgb coplo list 
from random import randint , choice

def generate_rgb_colors(num_colors):
    color_list = []
    for _ in range(num_colors):
        # Generate random RGB values in a list
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        color_list.append(color) #appendina in a list
    return color_list

# Example usage: generate 10 random RGB colors
color_list = generate_rgb_colors(10)

# Set up turtle graphics
t.colormode(255)
timmy = t.Turtle()  # Create an instance of the Turtle class as timmy 

# Change the pen color to white
timmy.pencolor((255, 255, 255))
# timmy.screen.bgcolor("black")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
#change the starting point 
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 101
# Draw a dot with a random color from the list
for dotcount in range(1,number_of_dots):
    timmy.dot(20, choice(color_list))
    timmy.forward(50)
    if dotcount %10 == 0 :
        
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

# Set up the screen and exit on click
screen = t.Screen()
screen.exitonclick()