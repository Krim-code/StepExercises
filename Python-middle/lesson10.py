import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os


def load_image():
    """
    Загружает выбранное изображение из списка в метку
    """
    # Получаем имя файла из выбора списка
    filename = listbox.get(listbox.curselection())

    # Открываем изображение и преобразуем его в формат, подходящий для Tkinter
    img = Image.open(filename)
    orig_width, orig_height = img.size

    # Изменяем размер изображения, сохраняя соотношение сторон изображения
    MAX_SIZE = 600
    scale = min(MAX_SIZE / orig_width, MAX_SIZE / orig_height)
    new_width = int(orig_width * scale)
    new_height = int(orig_height * scale)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    img_tk = ImageTk.PhotoImage(img)

    # Обновляем метку для отображения нового изображения
    image_label.config(image=img_tk)
    image_label.image = img_tk

    # Показываем исходное разрешение изображения
    root.title("Просмотр картинок - {}x{}".format(orig_width, orig_height))


def open_folder():
    """
    Открывает диалоговое окно выбора папки и загружает все изображения
    из этой папки в список
    """
    foldername = filedialog.askdirectory()

    # Очищаем список
    listbox.delete(0, tk.END)

    # Получаем все изображения в указанной папке
    images = [f for f in os.listdir(foldername) if
              os.path.isfile(os.path.join(foldername, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    # Добавляем изображения в список
    for img in images:
        listbox.insert(tk.END, os.path.join(foldername, img))


# Создаем окно
root = tk.Tk()
root.title("Просмотр картинок")

# Цвета для темной темы
bg_color = "#212121" # Цвет фона
fg_color = "#FFFFFF" # Цвет текста
bg_button_color = "#333333" # Цвет фона кнопок
fg_button_color = "#FFFFFF" # Цвет текста на кнопках

# Задаем цвета для окна и фрейма
root.config(bg=bg_color)
frame = tk.Frame(root, bg=bg_color)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Создаем кнопку для открытия папки с изображениями
open_button = tk.Button(root, text="Открыть папку", command=open_folder, bg=bg_button_color, fg=fg_button_color)
open_button.pack(pady=10)

# Задаем цвета для списка и полосы прокрутки
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, bg=bg_color)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=20, bg=bg_color, fg=fg_color, selectbackground=fg_color, selectforeground=bg_color)
scrollbar.config(command=listbox.yview, bg=bg_color)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Привязываем обработчик событий для изменения выбора списка
listbox.bind('<<ListboxSelect>>', lambda event: load_image())

# Задаем цвета для метки с изображением
image_label = tk.Label(root, bg=bg_color)
image_label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Запускаем приложение
root.mainloop()