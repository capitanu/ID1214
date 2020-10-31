from tkinter import *


class Box(object):
    name = ""
    box = None
    text = None
    def __init__(self, name, box, text):
        self.name = name
        self.box = box
        self.text = text

def make_box(name, box, text):
    return Box(name,box,text)

def move(canvas, box, text, x, y):
    canvas.coords(box, x, y, x+200, y+200)
    canvas.coords(text,x+100 ,y + 100)

    
def refresh_image(pile1, pile2, pile3, canvas, a_box, b_box, c_box, a_text, b_text, c_text ):
    print("hello world")


def main():
    master = Tk()
    canvas_width = 900
    canvas_height = 640
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    canvas.create_line(0, canvas_height - 20, canvas_width, canvas_height -20, fill="#476042")
    canvas_height = 620
    c_box = canvas.create_rectangle(50,canvas_height - 200, 250, canvas_height)
    b_box = canvas.create_rectangle(50,canvas_height - 400, 250, canvas_height -200 )
    a_box = canvas.create_rectangle(50,canvas_height - 600, 250, canvas_height - 400)
    c_text = canvas.create_text((150,canvas_height - 100), text = "C" ,font="Times 40")
    b_text = canvas.create_text((150,canvas_height - 300), text = "B" ,font="Times 40")
    a_text = canvas.create_text((150,canvas_height - 500), text = "A" ,font="Times 40")
    
    A = make_box("A", a_box, a_text)
    B = make_box("B", b_box, b_text)
    C = make_box("C", c_box, c_text)

    move(canvas, A.box, A.text, 350, canvas_height-200)
    
    pile_1 = [A, B, C, "floor"]
    pile_2 = ["floor"]
    pile_3 = ["floor"]

    
    
    mainloop()

main()
