import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        text_area.delete(1.0, "end")
        text_area.insert("end", text)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    text = text_area.get(1.0, "end")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def delete_text():
    text_area.delete(1.0, "end")

root = tk.Tk()
root.title("Текстовый редактор")

text_area = tk.Text(root)
text_area.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

delete_button = tk.Button(root, text="Удалить текст", command=delete_text)
delete_button.pack()

root.mainloop()