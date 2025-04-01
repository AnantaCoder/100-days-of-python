from tkinter import *
import random

root = Tk()
root.title("Typing Test")
root.geometry("800x600")
root.configure(bg="black")

class Timer:
    def __init__(self, master):
        self.master = master
        self.time_elapsed = 0
        self.running = False
        self.label = Label(master, text="Time: 0.00s", font=("Arial", 16), fg="white", bg="black")
        self.label.pack(pady=10)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.running:
            self.time_elapsed += 0.01
            self.label.config(text=f"Time: {self.time_elapsed:.2f}s")
            self.master.after(10, self.update_timer)

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="Time: 0.00s")

def writing_helper():
    possible_texts = [
        "Artificial intelligence has transformed the world, revolutionizing industries such as healthcare",
        "The universe remains one of the greatest mysteries, filled with billions of galaxies...",
        "The importance of reading cannot be overstated, as books provide knowledge, inspiration...",
        "Healthy eating is crucial for overall well-being, providing essential nutrients...",
        "Technology continues to evolve, reshaping daily life in profound ways...",
        "Music is a universal language that transcends cultural and linguistic barriers...",
        "Traveling broadens horizons, exposing individuals to new cultures, traditions..."
    ]
    return random.choice(possible_texts)

sample_text = writing_helper()

sample_display = Text(root, height=8, wrap=WORD, font=("Arial", 12), bg="black", fg="white")
sample_display.insert(END, sample_text)
sample_display.config(state=DISABLED)
sample_display.pack(pady=10, padx=20, fill=X)

input_text = Text(root, height=8, wrap=WORD, font=("Arial", 12), bg="white", fg="black")
input_text.pack(pady=10, padx=20, fill=X)

result_label = Label(root, text="", font=("Arial", 16), fg="white", bg="black")
result_label.pack(pady=10)

timer = Timer(root)

sample_display.tag_config('correct', background='#2ecc71')
sample_display.tag_config('incorrect', background='#e74c3c')
sample_display.tag_config('current', underline=True)

def update_highlights(input_content):
    sample_display.tag_remove('correct', '1.0', 'end')
    sample_display.tag_remove('incorrect', '1.0', 'end')
    sample_display.tag_remove('current', '1.0', 'end')

    input_len = len(input_content)
    sample_len = len(sample_text)
    compare_len = min(input_len, sample_len)

    for i in range(compare_len):
        start_idx = f"1.{i}"
        end_idx = f"1.{i+1}"
        if input_content[i] == sample_text[i]:
            sample_display.tag_add('correct', start_idx, end_idx)
        else:
            sample_display.tag_add('incorrect', start_idx, end_idx)

    if input_len < sample_len:
        current_idx = f"1.{input_len}"
        sample_display.tag_add('current', current_idx, f"{current_idx}+1c")

def on_key_release(event):
    input_content = input_text.get("1.0", "end-1c")
    
    if not timer.running and len(input_content) > 0:
        timer.start_timer()
    
    update_highlights(input_content)
    
    if input_content == sample_text:
        timer.running = False
        input_text.config(state=DISABLED)
        time_taken = timer.time_elapsed
        wpm = (len(sample_text.split()) / (time_taken / 60)) if time_taken > 0 else 0
        result_label.config(text=f"WPM: {wpm:.1f} | Accuracy: 100.00%")

input_text.bind("<KeyRelease>", on_key_release)

def reset_test():
    global sample_text
    sample_text = writing_helper()
    sample_display.config(state=NORMAL)
    sample_display.delete("1.0", END)
    sample_display.insert(END, sample_text)
    sample_display.config(state=DISABLED)
    input_text.config(state=NORMAL)
    input_text.delete("1.0", END)
    input_text.config(state=NORMAL)
    result_label.config(text="")
    timer.reset()

reset_btn = Button(root, text="New Test", command=reset_test, font=("Arial", 14), 
                  bg="#3498db", fg="white", activebackground="#2980b9")
reset_btn.pack(pady=10)

root.mainloop()