import turtle

# Set up the turtle and screen
turtleStar = turtle.Turtle()
turtleStar.color("gold")
sc = turtle.Screen()
sc.bgcolor("black")

# Draw a 5-pointed star
for s in range(5):
    turtleStar.forward(100)
    turtleStar.right(144)

# Reposition the turtle for the pentagon
turtleStar.penup()  # Lift the pen to avoid drawing while moving
turtleStar.left(36)
turtleStar.forward(62)
turtleStar.pendown()  # Put the pen down to start drawing again

# Draw a pentagon
for p in range(5):
    turtleStar.right(72)
    turtleStar.forward(62)

# Draw 5 circles at different orientations
for c in range(5):
    r = 50
    turtleStar.circle(r)
    turtleStar.right(100)

# Close the window when clicked
sc.exitonclick()
