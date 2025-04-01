from turtle import Turtle , Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

for i in range(100):
    timmy.forward(40)
    timmy.right(40)

myscreen = Screen()
print(myscreen.canvheight)
myscreen.exitonclick() #object methods 