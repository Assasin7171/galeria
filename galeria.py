import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

"""
https://tkdocs.com/tutorial/widgets.html
https://tkdocs.com/tutorial/index.html
"""
imgList = list()

folder_path = '../galeria/img'
for filename in os.listdir(folder_path):
    if filename.endswith(".JPG"):
        imgList.append(filename)

root = tk.Tk()
root.title("Galeria")
#root.geometry("800x600")
def do_Przodu():
    
    return


frame = ttk.Frame(root, borderwidth=5, relief="groove").grid(row=0, column=0)


img1 = ImageTk.PhotoImage(Image.open("img/8.JPG").resize([700, 500]))

labelImage = tk.Label(frame, image=img1).grid(row=1,column=0)

btnRight = tk.Button(root, text="Do przodu",command=do_Przodu).grid(sticky="E",row=2)
btnLeft = tk.Button(root, text="Do tyłu").grid(sticky="W",row=2)

root.mainloop()
