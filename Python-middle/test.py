import turtle

# Инициализация экрана и черепахи
screen = turtle.Screen()
t = turtle.Turtle()

# Рисуем круг
t.circle(50)

# Рисуем треугольник
for i in range(3):
    t.forward(100)
    t.left(120)

# Рисуем квадрат
for i in range(4):
    t.forward(100)
    t.left(90)

# Завершение программы
turtle.done()