import tkinter as tk

def click():
    entryText = txt.get()
    lbl.configure(text=f"привет, {entryText}")
    lbl.configure(font = ("Helvetica",20), fg='red')

window = tk.Tk()
window.title('hello')
window.geometry("400x250")

lbl = tk.Label(window,text='Введите имя',font=("arial",40))
lbl.grid(column=0,row=0)

txt = tk.Entry(window)
txt.grid(column=0,row=1)

btn = tk.Button(window,text='Подтвердить',command=click)
btn.grid(column=0,row=2)

window.mainloop()