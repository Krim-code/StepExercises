import tkinter as tk
from tkinter import filedialog
def open_file():
    file = filedialog.askopenfilename()
    with open(file,"r",encoding='utf-8') as f:
        text = f.read()
        text_area.delete(1.0,"end")
        text_area.insert("end",text)
def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    text = text_area.get(1.0,"end")
    with open(file,"w",encoding='utf-8') as f:
        f.write(text)
def delete_text():
    text_area.delete(1.0,"end")
# инициализируем главный модуль
root = tk.Tk()
root.title("Text Editor")
# cоздаём форму ввода
text_area = tk.Text(root)
text_area.pack()
# создаём меню
menu = tk.Menu(root)
#создаём подмодуль меню (файл)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
#добавляем подмодуль
menu.add_cascade(label="Файл",menu=file_menu)
root.config(menu=menu)

del_text = tk.Button(root, text = "Delete Text",command=delete_text)
del_text.pack()
root.mainloop()