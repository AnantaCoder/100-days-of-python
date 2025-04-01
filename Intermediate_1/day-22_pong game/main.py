from turtle import Screen, Turtle 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time


'''Main screen Features '''
screen = Screen()
# screen.bgcolor("black")
screen.bgpic('Days/Intermediate/day-22_pong game/back.gif')
screen.setup(width=800, height=600)
screen.title("Pong Game")

'''Middle Line'''
line = Turtle()
line.color("white")
line.hideturtle()
line.speed(50)
line.penup()
line.goto(0,300)
line.pendown()
line.goto(0,-300)


screen.tracer(0)   # hide the animation off , the auto update
screen.update() #update the screeen to show the paddle immidiately

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

#screen listens to user instructions

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
# screen.update()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
#middle boundry line 

#game mode
game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()

    #move the ball
    ball.move()
    
    #detecting the collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()