import tkinter as tk

def add():
    x = float(entry1.get())
    y = float(entry2.get())
    result = x + y
    result_label.config(text = f"Result: {result}", fg = "green")
def sub():
    x = float(entry1.get())
    y = float(entry2.get())
    result = x - y
    result_label.config(text=f"Result: {result}", fg="green")
def mul():
    x = float(entry1.get())
    y = float(entry2.get())
    result = x * y
    result_label.config(text=f"Result: {result}", fg="green")
def div():
    x = float(entry1.get())
    y = float(entry2.get())
    if y != 0:
        result = x / y
        result_label.config(text=f"Result: {result}", fg="green")
    else:
        result ="Ошибка при делении"
        result_label.config(text=f"Result: {result}", fg="red")


window = tk.Tk()
window.title('Калькулятор')

label1 = tk.Label(window, text='Введите первое число', font=("Impact", 16))
label1.pack(pady=5)
entry1 = tk.Entry(window, font=("Impact", 16), width=10, borderwidth=5)
entry1.pack(pady=5)

label2 = tk.Label(window, text='Введите второе число', font=("Impact", 16))
label2.pack(pady=5)
entry2 = tk.Entry(window, font=("Impact", 16), width=10, borderwidth=5)
entry2.pack(pady=5)

result_label = tk.Label(window, text="", font=("Impact", 16))
result_label.pack(pady=10)

add_button = tk.Button(window, text = "+", font=("Impact", 16), width=5,borderwidth=5,command=add)
add_button.pack(pady=5)

sub_button = tk.Button(window, text = "-", font=("Impact", 16), width=5,borderwidth=5,command=sub)
sub_button.pack(pady=5)

mul_button = tk.Button(window, text = "*", font=("Impact", 16), width=5,borderwidth=5,command=mul)
mul_button.pack(pady=5)

div_button = tk.Button(window, text = "/", font=("Impact", 16), width=5,borderwidth=5,command=div)
div_button.pack(pady=5)

window.mainloop()
