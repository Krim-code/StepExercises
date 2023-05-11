import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Текстовый редактор")

        self.text_area = tk.Text(master)
        self.text_area.pack()

        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.master.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.master.config(menu=menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, "r", encoding='utf-8') as file:
            text = file.read()
            self.text_area.delete(1.0, "end")
            self.text_area.insert("end", text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        text = self.text_area.get(1.0, "end")
        with open(file_path, "w",encoding='utf-8') as file:
            file.write(text)

    def delete_text(self):
        self.text_area.delete(1.0, "end")

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
