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




def main(move):
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

    
    spot1 = ['b', 'a', 'c', 'spot1']
    spot2 = ['spot2']
    spot3 = ['spot3']    

    
    mainloop()



on = {'a':'b', 'b':'c', 'c':'spot1'}
prev = {'a':'spot1', 'b':'spot1', 'c':'spot1'}
top = {'a':'spot1', 'spot2':'spot2', 'spot3':'spot3'}
spot = {'spot1':'spot1', 'spot2':'spot2', 'spot3':'spot3', 'a':'spot1', 'b':'spot1', 'c':'spot1'}
move = []

def preserve_alph_ord(A,B):
    if (A == 'a' or (A == 'b' and B == 'c') or B == 'spot1' or B == 'spot2' or B == 'spot3'): return True
    else: return False

def is_adjacent(A,B):
    Aspot = spot[A]
    Bspot = spot[B]
    if Aspot == Bspot or Aspot == 'spot2' or Bspot == 'spot2':
        return True
    else:
        return False

def clear_all(A,B):
    clear_off(A)
    clear_off(B)
    if on['a'] == A or on['b'] == A or on['c'] == A:
        clear_all(A,B)
    elif on['a'] == B or on['b'] == B or on['c'] == B:
        clear_all(A,B)
    else:
        return True


def put_on(A,B):
    if on[A] == B:
        return True
    else:
        if A == 'spot1': return False
        if A == 'spot2': return False
        if A == 'spot3': return False
        if A == B: return False
        if not(preserve_alph_ord(A,B)):
            clear_off(on[B])
            put_on(A,on[B])
        else:
            if not(is_adjacent(A,B)):
                for x,y in top.items():
                    if(y == 'spot2'):
                        put_on(A,x)
                        break
            clear_all(A,B)
            X = on[A]
            S = spot[X]
            spot[A] = S
            on[A] = B
            O = spot[X]
            prev[A] = O
            T = top[A]
            R = top[B]
            spot[A] = R
            del top[A]
            top[X] = T
            del top[B]
            top[A] = R
            move.append((A,X,B))


def reverse_find_top_helper(X):
    clear_off(X)
    S = spot[X]
    if S == 'spot1' or S == 'spot3':
        for x,y in top.items():
            if y == 'spot2':
                put_on(X,x)
                break
    elif prev[X] == 'spot1':
        for x,y in top.items():
            if y == 'spot3':
                put_on(X,x)
                break
    else:
        for x,y in top.items():
            if y == 'spot1':
                put_on(X,x)
                break
    
def clear_off(A):
        if on['b'] == A:
            reverse_find_top_helper('b')
        elif on['c'] == A:
            reverse_find_top_helper('c')
        elif on['a'] == A:
            reverse_find_top_helper('a')
        else: return True
            

def goal_state():
    put_on('c','spot3')
    put_on('b','c')
    put_on('a','b')


goal_state()
for i in move:
    print(i)

main(move)

