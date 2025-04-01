from turtle import Turtle,Screen
tim = Turtle()
sc = Screen()
#turtle colurs 
tim.shape("turtle")
tim.color("gold")
#screen color 
sc.bgcolor("black")


tim.width(10)
tim.speed(100)

col = ('gold', 'red' , 'cyan')

for i in range(500):
    tim.pencolor(col[i%3])
    tim.forward(i*5)
    tim.right(121)








#Screeen settings 
sc.exitonclick()