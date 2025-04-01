
'''GUI - GRAPHICAL USER INTERFACE'''




#turtle attributes
import turtle as t #alliss name 
from turtle import Turtle , Screen
timmy = Turtle()
screen = t.Screen()

screen.bgcolor("aqua")

timmy.shape("lund")



#python librarie modules  
import heroes
print(heroes.gen())


#turtle instructions 

#draw a square 

for i in range(4):
    timmy.forward(100)
    timmy.right(90)#what degree to rotate it to 


# Exit while clicking the screen 
screen.exitonclick()