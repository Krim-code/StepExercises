import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os


def load_image():
    filename = listbox.get(listbox.curselection())
    img = Image.open(filename)
    orig_width,orig_height = img.size

    MAX_SIZE = 600
    scale = min(MAX_SIZE/orig_width,MAX_SIZE/orig_height)
    new_width = int(orig_width*scale)
    new_height = int(orig_height * scale)
    img = img.resize((new_width,new_height),Image.ANTIALIAS)

    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image = img_tk)
    image_label.image = img_tk


def open_folder():
    foldername = filedialog.askdirectory()
    listbox.delete(0,tk.END)
    images = [f for f in os.listdir(foldername)
              if os.path.isfile(os.path.join(foldername,f)) and f.lower().endswith(('.png', '.jpg', '.jpeg','.bmp'))]
    for img in images:
        listbox.insert(tk.END,os.path.join(foldername,img))

root = tk.Tk()
root.title("Image Viewer")

bg_color = "#212121"
fg_color = "#FFFFFF"
bg_button_color = "#333333"
fg_button_color = "#FFFFFF"

root.config(bg=bg_color)
frame = tk.Frame(root, bg=bg_color)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

open_button = tk.Button(root, text="Открыть папку",
                        command=open_folder,bg =bg_button_color
                        ,fg = fg_button_color)
open_button.pack(pady=10)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, bg = bg_color)
listbox = tk.Listbox(frame,yscrollcommand=scrollbar.set, width=20,
                     bg = bg_color, fg = fg_color,
                     selectforeground=bg_color)
scrollbar.config(command=listbox.yview, bg = bg_color)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side = tk.LEFT,fill=tk.BOTH,expand=1)

listbox.bind('<<ListboxSelect>>',lambda event:load_image())

image_label = tk.Label(root, bg = bg_color)
image_label.pack(side = tk.RIGHT, fill= tk.BOTH, expand=1)

root.mainloop()
