from turtle import Turtle , Screen 
#turtle features & background 
timmy = Turtle()
scr= Screen()
scr.bgpic('Days\Intermediate\day-19_turtle game\imagess.gif')
timmy.shape("turtle")
timmy.color("aqua")
timmy.speed("fastest")

# #pattern of flower
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(50)
# Define functions to move the turtle in different directions
def move_forward():
    timmy.forward(20)

def move_backward():
    timmy.backward(20)

def turn_left():
    timmy.left(15)

def turn_right():
    timmy.right(15)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
# Listen for keyboard inputs
scr.listen()

# Bind keys to the functions- ( function_declaration , key_name )
scr.onkey(move_forward, "Up")     
scr.onkey(move_backward, "Down") 
scr.onkey(turn_left, "Left")     
scr.onkey(turn_right, "Right")   
scr.onkey(clear, "x")   
































#exit 
scr.exitonclick()