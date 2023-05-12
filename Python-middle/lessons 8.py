import tkinter as tk
from tkinter import filedialog

# def clicked():
#     lbl.configure(text="Foggot")

def clicked():
    entryText = f"hi {txt.get()}"
    lbl.configure(text = entryText)


# Create simple window
window = tk.Tk()
window.title('Test')


window.geometry('400x250')

lbl = tk.Label(window,text='Hello',font = ("Arial",50))
lbl.grid(column= 0, row= 0)

btn = tk.Button(window,text='Не нажимать',bg="black", fg="red" , command=clicked)
btn.grid(column=0, row= 2)

txt = tk.Entry(window)
txt.grid(column=0, row=1)


window.mainloop()