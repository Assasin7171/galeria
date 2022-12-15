import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

"""
https://tkdocs.com/tutorial/widgets.html
https://tkdocs.com/tutorial/index.html
"""


def openAllImg():
    for filename in os.listdir("files"):
        return
root = tk.Tk()
root.title("Galeria")
#root.geometry("800x600")

frame = ttk.Frame(root, borderwidth=5, relief="groove").grid(row=0, column=0)


img1 = ImageTk.PhotoImage(Image.open("img/zdj1.jpg").resize([700, 500]))
labelImage = tk.Label(frame, image=img1).grid(row=1,column=0)

btnRight = tk.Button(root, text="Do przodu").grid(sticky="E",row=2)
btnLeft = tk.Button(root, text="Do tyłu").grid(sticky="W",row=2)

root.mainloop()
