from tkinter import *
import math
#------------------------------IMAGE_INCLUDE---------------------------- #\
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2  #MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ----------------------------------- #
                                                                                
def reset_timer():
    window.after_cancel(timer)  # Cancel scheduling of function identified with ID
    canvas.itemconfig(timer_text, text='00:00')
    title_lable.config(text='Timer', fg=GREEN)
    check_lable.config(text='')
    global reps
    reps = 0
                                                                                
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        title_lable.config(text="Break", fg=RED)
        count_down(long_break_time)
    elif reps % 2 == 0:
        title_lable.config(text="Break", fg=PINK)
        count_down(short_break_time)
    else:
        title_lable.config(text="Work", fg=GREEN)
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60) #math.floor to the nearest integer 
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += CHECK_MARK
        check_lable.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("D:\\Anantacoder_python\\100days of code by Angela yu\\Days\\Intermediate\\day-28 dynamic typing and pomodoro gui\\pomodoro-start\\tomato.png")) #RESOURSE PATH TO THE RESOURSES
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_lable = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
title_lable.grid(column=1, row=0)

check_lable = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_lable.grid(column=1, row=3)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()