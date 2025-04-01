from tkinter import *
from PIL import Image, ImageDraw, ImageFont

root = Tk()
root.title("Watermark App")
root.geometry("800x600")
root.config(bg="white")

def add_watermark():
    image = Image.open(r'./day-85 watermark app/cat.jpeg')
    width, height = image.size
    draw = ImageDraw.Draw(image)
    text = "Ananta Coder"
    font = ImageFont.truetype("arial.ttf", 36)
    bbox = draw.textbbox((0, 0), text, font=font)
    textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = width - textwidth - 20
    y = height - textheight - 20
    draw.text((x, y), text, font=font, fill="white")
    image.save("watermarked_image.jpg")
    image.show()  

btn = Button(root, text="Add Watermark", command=add_watermark)
btn.pack(pady=20)
root.mainloop()
