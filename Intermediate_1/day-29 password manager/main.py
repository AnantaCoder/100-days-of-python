from tkinter import *
import customtkinter
from random import randint , choice , shuffle , choices
from tkinter import messagebox
import pandas.io.common
import pyperclip 
import pandas 
from read_panda import PasswordManager


PURPLE = '#640D5F'
RED = '#D91656'
PINK = '#EE66A6'
YELLOW = '#FFEB55'
FONT_NAME = 'Cursive'
MODERN_FONT = ("Monaco", 16, "bold italic")
FILEPATH = r'day-29 password manager\\Password_Database.csv'
# ---------------------------- SEARCH OPERATION --------------------------------- #
def search_window():
    search_int= Tk()
    search_int.title("Search Interface")
    new_window = Canvas(height=400 , width= 300 , bg="#26355D")
    frame = customtkinter.CTkFrame(master=search_int, width=380, height=280, corner_radius=15, fg_color="#3C4A6B")
    frame.pack(pady=5, padx=5)

    # Search Label, entry , button
    search_label = customtkinter.CTkLabel(master=frame, text="Enter Search Term:", text_color="white", font=("Helvetica", 20))
    search_label.pack(pady=10)
    search_entry = customtkinter.CTkEntry(master=frame, width=250, placeholder_text="Search...")
    search_entry.get()
    search_entry.pack(pady=10)
    def search_action():
        
        term =search_entry.get()
        manager = PasswordManager(FILEPATH)
        result = manager.search_credentials(term)
        messagebox.showinfo("Search Result : ", result)
        
    search_button = customtkinter.CTkButton(command = search_action,master=frame, text="Search", width=200)
    search_button.pack(pady=20)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list[1:15])

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
# ------------------------------------ SAVE PASSWORD ----------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    
    
    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave any empty fields")
    elif messagebox.askokcancel(title=website, message=f"You've entered: \nEmail: {email}\nPassword: {password}"f"\nIs it OK to save?"):
        data_remenber = {
        'WEBSITE': [website],
        'USERNAME/EMAIL': [email],
        'PASSWORD': [password]
    }
    new_storage = pandas.DataFrame(data_remenber)   
    new_storage.to_csv(r'day-29 password manager\Password_Database.csv', mode='a', index=0, header=not pandas.io.common.file_exists(r'day-29 password manager\Password_Database.csv'))
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Modern Password Manager')
window.config( pady=60 , bg=PURPLE)

canvas = Canvas(window, height=350, width=400, bg=PURPLE, highlightthickness=0)
lock_image = PhotoImage(file='day-29 password manager/locklogoo.png')
canvas.create_image(100, 200, image=lock_image)  
canvas.grid(column=1, row=0)

#website_label
website_label = Label(text="Website :",font=20  , fg = YELLOW, bg=PURPLE , highlightthickness=0)
website_label.grid(column=0, row=1, padx=5, pady=5, sticky="e")  # Align label to the right
website_entry = Entry(width=35)
website_entry.insert(0, "facebook.com")
website_entry.grid(column=1, row=1, padx=5, pady=5, columnspan=2, sticky="w")  # Align entry to the left
# website_entry.delete(0,END)
website_entry.focus() #move cussor to input field


# username entry 
username_label= Label(text="Username/Email :",font=20  , fg = YELLOW, bg=PURPLE , highlightthickness=0)
username_label.grid(column=0, row=3, padx=5, pady=5, sticky="e")
username_entry = Entry(width=35)
username_entry.insert(0, "anantacoder")
username_entry.grid(column=1, row=3, padx=5, pady=5, columnspan=2, sticky="w")  # Align entry to the left


#password entry  
Password_label= Label(text="Password :",font=20  , fg = YELLOW, bg=PURPLE , highlightthickness=0)
Password_label.grid(column=0, row=5, padx=5, pady=5, sticky="e")                
password_entry = Entry(width=17)
password_entry.insert(0, "Sample@123")
password_entry.grid(column=1, row=5, padx=5, pady=5, columnspan=2, sticky="w")


generate_button = Button(text= "Generate Password", width=20 , bg= YELLOW, font=("Helvetica", 10, "bold" ) , command=generate_random_password)
generate_button.grid(column=1, row=5, padx=5, pady=5)

add_button = Button(command=save,text= 'Add To the Database' , width= 40 ,bg= RED ,font= MODERN_FONT  )
add_button.grid(column=0 , row= 6 ,padx=5, pady=5 , columnspan=2)

# Search the t hiong
search_button = Button(command = search_window ,text = 'Search' , width = 30 ,bg= "#E0A75E" ,font= ("Comic Sans MS", 12, "normal"))
search_button.grid(column=0 , row= 67 ,padx=5, pady=5 , columnspan=2)



window.mainloop()