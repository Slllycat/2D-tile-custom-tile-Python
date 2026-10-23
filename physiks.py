import tkinter as tk
import random,json


empty=0
debug=1
tpf=1   #ticks per frame:good for more then 30 tiles
tbf=1   #time between frame:1-100   10 perfect normally
wm=0
brush=3
mx=0
my=0
biggness=1  #for tiles size per pixel
guib=1       #for interface size per pixel
size=30
size2=size**2
blocks=[]
temp=[]
stop=1

sttemp=20
direct=(+1,-1,+size,-size)#ways objects interact
names={     -1:"wall",                        0:"air",                    1:"water",                      2:"sand",                                   3:"wetsand",                  4:"ice",                    5:"watergas"}
color={     -1:"#000000",                   0:"#FFFFFF",              1:"#0000FF",                 2:"#FFFF00",                              3:"#CCCC00",                4:"#CCCCFF",              5:"#EEEEEE"}
hvn={       -1:255,                           0:0,                        1:1,                            2:1.5,                                      3:1.5,                        4:2,                        5:0.2}
wct={       -1:[["x","x"],["x","x"]],         0:[["x","x"],["x","x"]],    1:[[-1,100],[4,5]],             2:[["x","x"],["x","x"]],                    3:[["x","x"],["x","x"]],      4:[["x",1],["x",1]],        5:[[95,"x"],[1,"x"]]}
wrm={       -1:0,                             0:1,                        1:60,                           2:55,                                       3:70,                         4:75,                       5:15}
mvb={       -1:[],                            0:[],                       1:[("x",-size),(2,-1),(1,+1)],  2:[("x",-size),(1,-size-1),(1,-size+1)],    3:[("x",-size)],              4:[],                       5:[(20,-size),(16,size),(20,-1),(16,+1)]}
#el1,el2,chance,el1,el2,temp%,temp%
itr=[(1,2,1,0,3,0,1)]

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
            if empty:
                blocks.append(1)
            else:
                blocks.append(random.randint(0,4))
        blocks.append(-1)
    for i in range(size):
        blocks.append(-1)
    for i in range(size2):
        temp.append(sttemp)

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
    global cube,blocks,biggness,brush,stop
    x = 0
    y = 10*size*biggness
    weg = 0
    tiles=10*biggness
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if debug==1:
                cube = canvas.create_rectangle(x, y, x + tiles, y - tiles, fill=color[blocks[weg]],outline=color[blocks[weg]])
            elif debug==2:
                cc=gradient_color(temp[weg],min(temp),max(temp))
                cube = canvas.create_rectangle(x, y, x + tiles, y - tiles, fill=cc,outline=cc)
            if stop:
                tick(weg)
            weg = weg + 1
            x =x+tiles
        x=0
        y=y- tiles
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

def changetemp(amount):
    global mx,my,brush,blocks,biggness,temp
    tiles=10*biggness
    if round((my-5)/tiles)>=1 and round((my-5)/tiles)<=size-2 and round((mx-5)/tiles)>=1 and round((mx-5)/tiles)<=size-2:
        temp[(round((mx-5)/tiles))+(size-round((my-5)/tiles)*size-size*2)]+=amount

def gradient_color(value, min_value, max_value):
    if max_value == min_value:
        return "#00FF00"  # avoid division by zero

    # Normalize to 0-1
    t = (value - min_value) / (max_value - min_value)
    t = max(0, min(1, t))  # clamp

    if t < 0.5:
        # Blue -> Green
        local = t * 2
        r = 0
        g = int(255 * local)
        b = int(255 * (1 - local))
    else:
        # Green -> Red
        local = (t - 0.5) * 2
        r = int(255 * local)
        g = int(255 * (1 - local))
        b = 0

    return f"#{r:02x}{g:02x}{b:02x}"

def mouse_click(event):
    draw()
canvas.bind("<Button-1>", mouse_click)


def move(event):
    global debug,tmp,stop
    if event.keysym=="space":
        draw()
    elif event.keysym=="s":
        stop=1-stop
    elif event.keysym=="1":
        debug=1
    elif event.keysym=="2":
        debug=2
    elif event.keysym=="plus":
        changetemp(+3)
    elif event.keysym=="asterisk":
        changetemp(+45)
    elif event.keysym=="minus":
        changetemp(-3)
    elif event.keysym=="underscore":
        changetemp(-45)
    else:
        print(event.keysym)
    print(round(sum(temp),2),round(min(temp),2),round(max(temp),2))
window.bind("<Key>", move)

def tick(weg):
    global blocks,tmp
    typ=blocks[weg]
    for i in mvb[typ]:
        ch,dur=i
        if ch=="x" or random.randint(0,ch)==0:
            typ=blocks[weg]
            if hvn[blocks[weg+dur]]<hvn[typ]:
                a=blocks[weg+dur]
                blocks[weg+dur]=typ
                blocks[weg]=a
                temp[weg],temp[weg+dur]=temp[weg+dur],temp[weg]

    for i in itr:
        typ=blocks[weg]
        if typ==i[0]:
            for i2 in direct:
                if blocks[weg+i2]==i[1]:
                    if random.randint(0,i[2])==0:
                        blocks[weg],blocks[weg+i2]=i[3],i[4]
                        t=temp[weg]+temp[weg+i2]
                        temp[weg],temp[weg+i2]=t*i[5],t*i[6]

    typ=blocks[weg]
    if wrm[typ]>0:
        i=random.choice(direct)
        t=min(wrm[typ],wrm[blocks[weg+i]])
        d=((temp[weg+i]-temp[weg])/2)*(t/100)
        temp[weg]+=d
        temp[weg+i]-=d

    tmp=wct[blocks[weg]]
    if tmp[0][0]!="x" and tmp[0][0]>temp[weg]:
        blocks[weg]=tmp[1][0]
    if tmp[0][1]!="x" and tmp[0][1]<temp[weg]:
        blocks[weg]=tmp[1][1]

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
