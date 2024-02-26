import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()

width = 500
height = 500

canvas = tk.Canvas(root, width=width, height=height)

root.geometry(f"{width}x{height}")
root.title("DISCIPLINE !!!")

title = tk.Label(root, text="Solve atleast 3 Questions !!", font=("Arial", 12))
title.pack(pady=12)

image = Image.open("bg.jpg")
image = image.resize((width, height))

photo_image = ImageTk.PhotoImage(image)

label = tk.Label(canvas, image=photo_image)

canvas.create_window(0, 0, anchor="nw", window=label)

canvas.pack(padx=4, pady=0)

def confo():
    msg = messagebox.askquestion(title="DO IT!!", message="DID YOU SOLVED ?")
    if(msg == "yes"):
        root.destroy()
    else:
        print("Seriously bro?")

root.protocol("WM_DELETE_WINDOW", confo)

root.mainloop()