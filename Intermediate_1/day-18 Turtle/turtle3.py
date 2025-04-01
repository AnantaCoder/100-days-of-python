from turtle import Turtle,Screen
tim = Turtle()
sc = Screen()
#turtle colurs 
tim.shape("turtle")
tim.color("gold")
#screen color 
sc.bgcolor("black")


#shape - gon 

# sides = 8
# angle  = 360/sides
# while angle!= 10:
    
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(angle)#what degree to rotate it to 
#     angle += 5

# PENTAGON 
sides = 5
angle  = 360/sides

while angle==angle:    
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)#what degree to rotate it to 
    angle += 5

#Screeen settings 
sc.exitonclick()