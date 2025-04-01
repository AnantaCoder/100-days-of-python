from turtle import Turtle, Screen
import random

# Initialize the race condition
is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
#text input
user_bet=screen.textinput(
    title="The Turtle racing Satta",
    prompt="Which Turtle will won? Color?").lower()

#set turtle , positions 
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
each_turtles = []
y_positions = [-250, -150, -50, 50, 150, 250]

#create turtles (6)
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[i])
    new_turtle.goto(x= -450, y = y_positions[i])
    each_turtles.append(new_turtle)

#if user made a bet
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in each_turtles:
        if turtle.xcor() > 450:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've made a correct bet! The {winning_color} turtle is the winner🏆🏆🏆")
            else:
                print(f"you have lost the Race. {winning_color} WON 🏆")
            is_race_on = False
        #move by random distance 
        move_distance = random.randint(0,11)
        turtle.forward(move_distance)
#exit()
screen.exitonclick()