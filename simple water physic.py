import tkinter as tk
import random

brush=1
mx=0
my=0
size = 25
size2 = size**2
blocks = []


window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * 10+40) + "x" + str(size * 10))
canvas = tk.Canvas(window, width=(size * 10+40), height=(size * 10), bg="white")
canvas.pack()


def reset():
    for i in range(size):
        blocks.append(-1)
    for i in range(size-2):
        blocks.append(-1)
        for i in range(size-2):
            blocks.append(random.randint(0,1))
        blocks.append(-1)
    for i in range(size):
        blocks.append(-1)

reset()


#mouse pos
def mouse_pos(event):
    global mx, my
    mx, my = event.x, event.y
canvas.bind("<Motion>", mouse_pos)


def render():
    global cube,blocks
    x = 0
    y = 10*size
    weg = 0
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if blocks[weg] == 1:
                cube = canvas.create_rectangle(x, y, x + 10, y - 10, fill="blue",outline="blue")
            elif blocks[weg] == -1:
                cube = canvas.create_rectangle(x, y, x + 10, y - 10, fill="black")
            else:
                cube = canvas.create_rectangle(x, y, x + 10, y - 10, fill="white",outline="white")
            weg = weg + 1
            x = x + 10
        x = 0
        y = y - 10
    cube = canvas.create_rectangle(size*10, size*10-25, size*10+25, size*10-50, fill="blue")

    cube = canvas.create_rectangle(size*10, size*10-75, size*10+25, size*10-100, fill="white")

    cube = canvas.create_rectangle(size*10, size*10-125, size*10+25, size*10-150, fill="black")
    window.after(1, tick)



def mouse_click(event):
    global mx,my,brush,blocks
    if mx >=(size *10):
        if mx >=(size *10) and mx<=(size*10+25) and my <=(size *10-25) and my>=(size*10-50):
            brush=1
        elif mx >=(size *10) and mx<=(size*10+25) and my <=(size *10-75) and my>=(size*10-100):
            brush=0

        elif mx >=(size *10) and mx<=(size*10+25) and my <=(size *10-125) and my>=(size*10-150):
            brush=-1
    else:
        if round((my-5)/10)>=1 and round((my-5)/10)<=23 and round((mx-5)/10)>=1 and round((mx-5)/10)<=23:
            blocks[(round((mx-5)/10))+(size-round((my-5)/10)*size-size*2)]= brush

canvas.bind("<Button-1>", mouse_click)

def tick():
    global cube,blocks
    x = 0
    y = 10+size
    weg = 0
    for i in range(size):
        for i in range(size):
            if blocks[weg] ==1:
                if blocks[weg-size] == 0 :
                    blocks[weg-size] = 1
                    blocks[weg] = 0
                else:
                    r= random.randint(1,2)
                    if r ==1 and blocks[weg+1]==0:
                        blocks[weg+1] = 1
                        blocks[weg] = 0
                    elif r ==2 and blocks[weg-1]==0:
                        blocks[weg-1] = 1
                        blocks[weg] = 0
            weg = weg + 1
            x = x + 10
        x = 0
        y = y - 10
    window.after(1, render)





render()
window.mainloop()# Schreibe hier Deinen Code :-)
