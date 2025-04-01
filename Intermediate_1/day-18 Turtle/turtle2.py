from turtle import Turtle, Screen

# Create the turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("gold")

# Create the screen object
screen = Screen()

# Define a function to move the turtle to the clicked position
def move_to_click(x, y):
    timmy.goto(x, y)

# Set up the screen to listen for clicks and move the turtle
screen.onclick(move_to_click)

# Keep the window open until it's closed
screen.mainloop()
