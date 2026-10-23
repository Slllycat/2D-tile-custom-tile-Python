import tkinter as tk
import random



tpf=2   #ticks per frame:good for more then 30 tiles
tbf=10   #time between frame:1-100   10 perfect normally
wm=0
brush=1
mx=0
my=0
biggness=2  #for tiles size per pixel
guib=2       #for interface size per pixel
size = 25
size2 = size**2
blocks = []


window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * 10*biggness+40*guib) + "x" + str(size*biggness * 10))
canvas = tk.Canvas(window, width=(size * 10*biggness+40*guib), height=(size * 10*biggness), bg="white")
canvas.pack()


def reset():
    for i in range(size):
        blocks.append(-1)
    for i in range(size-2):
        blocks.append(-1)
        for i in range(size-2):
            blocks.append(random.randint(0,2))
        blocks.append(-1)
    for i in range(size):
        blocks.append(-1)

reset()


#mouse pos
def mouse_pos(event):
    global mx, my
    mx, my = event.x, event.y
canvas.bind("<Motion>", mouse_pos)



def Mainloop():
    global wm,tpf,tbf
    if wm==0:
        for _ in range(tpf):
            render()
    else:
        wm-=1
    window.after(tbf, Mainloop)


def render():
    global cube,blocks,biggness,brush
    x = 0
    y = 10*size*biggness
    weg = 0
    tiles=10*biggness
    color=["black","white","blue","yellow"]
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            cube = canvas.create_rectangle(x, y, x + tiles, y - tiles, fill=color[blocks[weg]+1],outline=color[blocks[weg]+1])
            tick(weg)
            weg = weg + 1
            x = x + tiles
        x = 0
        y = y - tiles
    if brush!=1:out="black"
    else:out="purple"
    cube = canvas.create_rectangle(size*tiles, size*tiles-25*guib, size*tiles+25*guib, size*tiles-50*guib, fill="blue",outline=out)
    if brush!=0:out="black"
    else:out="purple"
    cube = canvas.create_rectangle(size*tiles, size*tiles-75*guib, size*tiles+25*guib, size*tiles-100*guib, fill="white",outline=out)
    if brush!=-1:out="black"
    else:out="purple"
    cube = canvas.create_rectangle(size*tiles, size*tiles-125*guib, size*tiles+25*guib, size*tiles-150*guib, fill="black",outline=out)
    if brush!=2:out="black"
    else:out="purple"
    cube = canvas.create_rectangle(size*tiles, size*tiles-175*guib, size*tiles+25*guib, size*tiles-200*guib, fill="yellow",outline=out)


def draw():
    global mx,my,brush,blocks,biggness
    tiles=10*biggness
    if mx >=(size *tiles):
        if mx >=(size *tiles) and mx<=(size*tiles+25*guib) and my <=(size *tiles-25*guib) and my>=(size*tiles-50*guib):
            brush=1
        elif mx >=(size *tiles) and mx<=(size*tiles+25*guib) and my <=(size *tiles-75*guib) and my>=(size*tiles-100*guib):
            brush=0

        elif mx >=(size *tiles) and mx<=(size*tiles+25*guib) and my <=(size *tiles-125*guib) and my>=(size*tiles-150*guib):
            brush=-1
        elif mx >=(size *tiles) and mx<=(size*tiles+25*guib) and my <=(size *tiles-175*guib) and my>=(size*tiles-200*guib):
            brush=2
    else:
        if round((my-5)/tiles)>=1 and round((my-5)/tiles)<=size-2 and round((mx-5)/tiles)>=1 and round((mx-5)/tiles)<=size-2:
            blocks[(round((mx-5)/tiles))+(size-round((my-5)/tiles)*size-size*2)]= brush


def mouse_click(event):
    draw()
canvas.bind("<Button-1>", mouse_click)


def move(event):
    if event.keysym=="space":
        draw()
window.bind("<Key>", move)

def tick(weg):
    global blocks
    x = 0
    y = 10+size
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
    elif blocks[weg] ==2:
        if blocks[weg-size] == 0 or blocks[weg-size] == 1:
            a=blocks[weg-size]
            blocks[weg-size] = 2
            blocks[weg] = a
        else:
            r= random.randint(1,2)
            if r ==1 and (blocks[weg+1-size]==0 or blocks[weg+1-size]==1):
                a=blocks[weg+1-size]
                blocks[weg+1-size] = 2
                blocks[weg] = a
            elif r ==2 and (blocks[weg-1-size]==0 or blocks[weg-1-size]==1):
                a=blocks[weg-1-size]
                blocks[weg-1-size] = 2
                blocks[weg] = a

last_pos = [window.winfo_x(), window.winfo_y()]
def windowmove(event):
    global wm
    x, y = window.winfo_x(), window.winfo_y()
    if (x, y) != tuple(last_pos):
        last_pos[0], last_pos[1] = x, y
        wm=50

window.bind("<Configure>", windowmove)




Mainloop()
window.mainloop()# Schreibe hier Deinen Code :-)
# Schreibe hier Deinen Code :-)
