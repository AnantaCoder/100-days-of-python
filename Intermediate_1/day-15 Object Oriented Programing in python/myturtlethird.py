import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "robot"
robot = turtle.Turtle()
robot.speed(5)

# Function to draw a rectangle
def draw_rectangle(turtle, width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a circle
def draw_circle(turtle, radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Draw the head (rectangle)
robot.penup()
robot.goto(-100, 100)
robot.pendown()
robot.pencolor("black")
draw_rectangle(robot, 200, 200, "gray")

# Draw the left eye (circle)
robot.penup()
robot.goto(-60, 170)
robot.pendown()
draw_circle(robot, 30, "white")

# Draw the right eye (circle)
robot.penup()
robot.goto(60, 170)
robot.pendown()
draw_circle(robot, 30, "white")

# Draw the left eye pupil (smaller circle)
robot.penup()
robot.goto(-60, 180)
robot.pendown()
draw_circle(robot, 10, "black")

# Draw the right eye pupil (smaller circle)
robot.penup()
robot.goto(60, 180)
robot.pendown()
draw_circle(robot, 10, "black")

# Draw the mouth (rectangle)
robot.penup()
robot.goto(-50, 60)
robot.pendown()
draw_rectangle(robot, 100, 30, "black")

# Draw the antenna base (small rectangle)
robot.penup()
robot.goto(-15, 100)
robot.pendown()
draw_rectangle(robot, 30, 10, "black")

# Draw the antenna (line)
robot.penup()
robot.goto(0, 110)
robot.pendown()
robot.pensize(5)
robot.setheading(90)
robot.forward(50)

# Draw the antenna tip (small circle)
robot.penup()
robot.goto(0, 160)
robot.pendown()
draw_circle(robot, 10, "red")

# Hide the turtle and finish
robot.hideturtle()
screen.exitonclick()
