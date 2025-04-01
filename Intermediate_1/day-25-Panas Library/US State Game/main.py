import pandas as pd 
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

    
data = pd.read_csv(r'Days/Intermediate/day-25-Panas Library/US State Game/50_states.csv')


screen.title('USA State Games ')
image = r'Days/Intermediate/day-25-Panas Library/US State Game/blank_states_img.gif'
screen.addshape(image)
# turtle.shape(image)
screen.bgpic(image)
turtle.hideturtle()
turtle.penup()
turtle.color('red')

missing_states = []
guessed_states = []
states_list = data.state.to_list()
x_axis_list = data.x.to_list()
y_axis_list = data.y.to_list()



    # main loop for name gueesser 
while len(guessed_states) < 50:
        answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Name a State").title()

        
    
        if answer is None:
            print("User cancelled the input")
            continue
        
    
        if answer in states_list and answer not in guessed_states:
            
            guessed_states.append(answer) # Tracking the guessewd states
            answer_index = states_list.index(answer)
            x_coordinate = x_axis_list[answer_index]
            y_coordinate = y_axis_list[answer_index]
            turtle.goto(x_coordinate, y_coordinate)
            turtle.write(answer , align='center' ,  font= ("Arial" ,8,'normal'))
            
        elif answer == 'Exit':
            break

        
        
screen.mainloop()


'''
To check if an element is already present in a list, you can use the in keyword in Python. It returns True if the element is present in the list, and False otherwise.'''