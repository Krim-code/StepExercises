from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import Image, ImageDraw

def use_pen():
    activate_button(pen_button)
def use_brush():
    activate_button(brush_button)
def choose_color():
    global eraser_on, color
    eraser_on = False
    color = askcolor(color=color)[1]
def use_eraser():
    activate_button(eraser_button,eraser_mode=True)
def activate_button(some_button,eraser_mode = False):
    global eraser_on, active_button
    active_button.config(relief = RAISED)
    some_button.config(relief = SUNKEN)
    eraser_on = eraser_mode
def paint(event):
    global old_x, old_y, line_width, color, eraser_on
    line_width = choose_size_button.get()
    paint_color = 'white' if eraser_on else color
    if old_x and old_y:
        c.create_line(old_x,old_y, event.x, event.y,
                      width=line_width,
                      fill=paint_color,
                      capstyle=ROUND,
                      smooth=TRUE)
        img_draw.line([old_x,old_y, event.x, event.y],
                      width=line_width,fill=paint_color)
    old_x = event.x
    old_y = event.y
def reset(event):
    global old_x ,old_y
    old_x,old_y = None,None
def save_img():
    global img, img_draw
    filename = filedialog.asksaveasfilename( defaultextension='.png')
    if filename:
        img.save(filename)
def main():
    global pen_button, brush_button, color_button, eraser_button, choose_size_button, c
    global root, old_x, old_y, line_width, color, eraser_on, active_button
    global img, img_draw

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    root = Tk()

    old_x = None
    old_y = None
    line_width = DEFAULT_PEN_SIZE
    color = DEFAULT_COLOR
    eraser_on = False
    active_button = None

    pen_button = Button(root, text="pen",command=use_pen)
    pen_button.grid(row=0, column = 0)

    brush_button = Button(root, text="brush", command=use_brush)
    brush_button.grid(row=0, column=1)

    color_button = Button(root, text="color", command=choose_color)
    color_button.grid(row=0, column=2)

    eraser_button = Button(root, text="eraser", command=use_eraser)
    eraser_button.grid(row=0, column=3)

    choose_size_button = Scale(root, from_=1, to=50,orient=HORIZONTAL)
    choose_size_button.grid(row=0,column=4)

    save_button = Button(root, text="save", command=save_img)
    save_button.grid(row=0, column=5)

    c = Canvas(root,bg='white',width = 600, height =600)
    c.grid(row=1, columnspan=6)

    active_button = pen_button

    c.bind('<B1-Motion>',paint)
    c.bind('<ButtonRelease-1>',reset)

    img = Image.new('RGB',(600,600),(255,255,255))
    img_draw = ImageDraw.Draw(img)


    root.mainloop()


main()
