import tkinter as tk
from turtle import color

count = 0
def clicked():
    global count
    count += 1
    lbl.configure(text = f'{count} ')

window = tk.Tk()
window.title('Test')
window.geometry('400x250')

lbl = tk.Label(window, text='Hello, world', font=('Arial', 50))
lbl.grid(column=0, row=0)

btn = tk.Button(window, text='Click', command=clicked, bg="red", fg="white")
btn.grid(column=0, row=1)

window.mainloop()
