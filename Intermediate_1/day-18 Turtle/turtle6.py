from turtle import Turtle,Screen
from random import choice

tim = Turtle()
sc = Screen()
#turtle colurs 
tim.shape("turtle")
tim.color("gold")
#screen color 
sc.bgcolor("black")


tim.width(2)
tim.speed(22)

colors = [
    "red", "green", "blue", "yellow", "purple", "orange", 
    "pink", "brown", "black", "white", "cyan", "magenta", 
    "gold", "silver", "coral", "turquoise", "navy", "olive", 
    "teal", "violet"
]

#shapes 
def draw_shape (num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
    tim.color(choice(colors))







#Screeen settings 
sc.exitonclick()