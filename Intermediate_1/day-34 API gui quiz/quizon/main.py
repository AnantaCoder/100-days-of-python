#----------------------qUIZ-ON---------------------------------
from tkinter import *
import random
import customtkinter as ctk
from PIL import Image , ImageTk
import requests
import html

MODERN_FONT = ("Comic Sans MS", 30, "bold")

#----------------------- API ---------------------------------
response = requests.get('https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=boolean')
print(response.raise_for_status())
data = response.json()
question = data['results'][0]['question']
ans = data['results'][0]['correct_answer']

#----------------------- LOGIC ---------------------------------



score = 0 
question_index = 0
total_question = 20
def on_yes():
    check_answ(True)
def on_no():
    check_answ(False)

def check_answ(user_ans):
    global score 
    global question_index
    # global total_question
    ans = data['results'][question_index]['correct_answer'] == "True"  
    
    if user_ans == ans:
        score += 1 
    print(f"Current score: {score}") 
    screen.itemconfig(score_tracker , text = f' Score :{score}/{total_question}')
    
    question_index += 1 
    if question_index < total_question:
        next_question()       
    else:
        end_quiz()
def next_question():
    question = html.unescape(data['results'][question_index]['question']) #convrt the signs to the human redable
    screen.itemconfig(question_text, text= question)

def end_quiz():
    screen.itemconfig(question_text, text="Quiz Over" , font =("Comic Sans MS", 45, "bold") )
    # print(f'final score is:{score}/{total_question}')
#------------------------ INTERFACE -----------------------------
window = Tk()
window.title("Quiz ON")
window.config(padx=50 , pady= 40, bg='#222831')

screen = Canvas(window, height=600 , width=500 ,bg= '#222831', highlightthickness=0)

logo = 'day-34 API gui quiz//quizon//chest_tresure.png'
yes_img = 'day-34 API gui quiz//quizon//yes_img.png'
no_img = 'day-34 API gui quiz//quizon//no_img.png'


main_logo = Image.open(logo)
resize_img= main_logo.resize((250, 250)) 
background_img = ImageTk.PhotoImage(resize_img)
screen.create_image(250, 125, image=background_img)
 
screen.grid(row=5,column=0  , padx= 50 ,pady=15,columnspan=2  )
screen.create_text(250,270,text="Quiz On : GK Edition" , font=MODERN_FONT , fill= '#EEEEEE')

resize_yes = Image.open(yes_img).resize((100,100))
resize_no = Image.open(no_img).resize((100,100))


yes_image = ImageTk.PhotoImage(resize_yes)
no_image = ImageTk.PhotoImage(resize_no)



yes_button = Button(window, image=yes_image, command=on_yes, borderwidth=0, highlightthickness=0)  # Use yes_image
no_button = Button(window, image=no_image, command=on_no, borderwidth=0, highlightthickness=0)
yes_button.grid(row=6, column=0, padx=50, pady=(15, 5))
no_button.grid(row=6, column=1, padx=50, pady=(15, 5))  


question_text = screen.create_text(200, 400, text=question, width=400, font=("Comic Sans MS", 15, "bold"), fill="#00ADB5")
yes_button.image = yes_image
no_button.image = no_image

score_tracker = screen.create_text(250, 330 , text = f'Score :{score}/{total_question}', font=("Comic Sans MS", 15, "bold") , fill='#FB773C' )








window.mainloop()
