import tkinter 

window = tkinter.Tk()
window.title("my first gui programe")
window.minsize(width=500, height=300)

#components 
#label 

mylable=tkinter.Label(text= 'Txt', font=("Arial" , 24, "bold"))
# mylable.pack(side= 'left', expand=True) #center the lable 
mylable.pack()

#button 
def btn_clicked():
    print("button was clicked")
    input_text=input.get()
    mylable.config(text=input_text)
b =tkinter.Button(text='Click me ' , command=btn_clicked)
b.pack()

#enty 

input = tkinter.Entry(width = 25)
input.pack()
# input.get()







# keep it on 
window.mainloop()