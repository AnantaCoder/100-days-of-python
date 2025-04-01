import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle named "designer"
designer = turtle.Turtle()
designer.shape("turtle")
designer.speed(10)

# Set the turtle's color
designer.pencolor("cyan")

# Function to draw a circle pattern
def draw_circle_pattern(radius, angle):
    for _ in range(int(360 / angle)):
        designer.circle(radius)
        designer.left(angle)

# Draw the first circle pattern
draw_circle_pattern(100, 10)

# Move the turtle to a new position
designer.penup()
designer.goto(-200, -200)
designer.pendown()

# Draw the second circle pattern with a different radius
draw_circle_pattern(50, 10)

# Move the turtle to another position
designer.penup()
designer.goto(200, 200)
designer.pendown()

# Draw the third circle pattern with a different radius
draw_circle_pattern(150, 15)

# Hide the turtle and display the design
designer.hideturtle()
screen.exitonclick()
