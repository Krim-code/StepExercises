import tkinter as tk

# Создание окна
window = tk.Tk()
window.title("Калькулятор")



# Создание виджетов для ввода чисел
label1 = tk.Label(window, text="Введите первое число:", font=('Arial', 16))
label1.pack(pady=5)
entry1 = tk.Entry(window, font=('Arial', 16), width=10, borderwidth=5)
entry1.pack(pady=5)

label2 = tk.Label(window, text="Введите второе число:", font=('Arial', 16))
label2.pack(pady=5)
entry2 = tk.Entry(window, font=('Arial', 16), width=10, borderwidth=5)
entry2.pack(pady=5)

# Создание виджета для вывода результата
result_label = tk.Label(window, text="", font=('Arial', 16))
result_label.pack(pady=10)

# Создание функций для операций
def add():
    x = float(entry1.get())
    y = float(entry2.get())
    result = x + y
    result_label.config(text=f"Результат: {result}", fg='blue')

def subtract():
    x = float(entry1.get())
    y = float(entry2.get())
    result = x - y
    result_label.config(text=f"Результат: {result}", fg='blue')

def multiply():
    x = float(entry1.get())
    y = float(entry2.get())
    result = x * y
    result_label.config(text=f"Результат: {result}", fg='blue')

def divide():
    x = float(entry1.get())
    y = float(entry2.get())
    if y != 0:
        result = x / y
        result_label.config(text=f"Результат: {result}", fg='blue')
    else:
        result_label.config(text="Ошибка: деление на ноль", fg='red')

# Создание кнопок
add_button = tk.Button(window, text="+", font=('Arial', 16), width=5, borderwidth=5, command=add)
add_button.pack(pady=5)

subtract_button = tk.Button(window, text="-", font=('Arial', 16), width=5, borderwidth=5, command=subtract)
subtract_button.pack(pady=5)

multiply_button = tk.Button(window, text="*", font=('Arial', 16), width=5, borderwidth=5, command=multiply)
multiply_button.pack(pady=5)

divide_button = tk.Button(window, text="/", font=('Arial', 16), width=5, borderwidth=5, command=divide)
divide_button.pack(pady=5)

# Запуск приложения
window.mainloop()