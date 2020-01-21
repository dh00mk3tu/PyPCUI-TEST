import tkinter as tk
from tkinter import *
import webbrowser

frame = tk.Tk()
frame.title("Web Browser Test v1")
frame.geometry("400x100")

def instagram():
    webbrowser.open("www.instagram.com/dh00mk3tu")

instagram = PhotoImage(file="instagram.png")
instagram_btn = tk.Button(frame, image=instagram, command=instagram)
instagram_btn.grid(row=0, column=1)

frame.mainloop()
