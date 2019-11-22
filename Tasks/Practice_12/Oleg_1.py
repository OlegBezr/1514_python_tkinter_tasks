import tkinter
import random
import math

main = tkinter.Tk()
main.title('smth')
sSize = 800
canvas = tkinter.Canvas(main, bg = "white", height = sSize, width = sSize)
canvas.pack()

def drawAxes():
    canvas.create_line((0, sSize / 2), (sSize, sSize/2), fill = 'black', width = 3)
    canvas.create_line((sSize / 2, 0), (sSize/2, sSize), fill = 'black', width = 3)

label = tkinter.Label(main, text = "smth")
label.pack()

def xs(x):
    return sSize//2 + x
def ys(y):
    return sSize//2 - y

def putpixel(x, y, color):
    canvas.create_line((x, y), (x+1, y), fill=color, width = 3)

def moveto(x, y):
    graph_pos[1] = x
    graph_pos[2] = y
def lineto(x, y, width=1, color='black'):
    graph_pos[0].create_line(graph_pos[1:], (x, y), width=width, fill=color)
    graph_pos[1] = x
    graph_pos[2] = y
    
def draw(event):
    #print(event.keycode)
    canvas.delete('all')
    drawAxes()
    typ = event.keycode
    if (typ == 83):
        SIN()
    elif (typ == 67):
        COS()
    elif (typ == 84):
        TAN()
    
def SIN():
    label.config(text = "SIN")
    for x in range(-sSize//2-1, sSize//2 + 1):
        putpixel(xs(x), ys(50 * math.sin(x*math.pi/180)), 'blue')
        
def COS():
    label.config(text = "COS")
    for x in range(-sSize//2-1, sSize//2 + 1):
        putpixel(xs(x), ys(50 * math.cos(x*math.pi/180)), 'blue')    
        
def TAN():
    label.config(text = "TAN")
    for x in range(-sSize//2-1, sSize//2 + 1):
        putpixel(xs(x), ys(50 * math.tan(x*math.pi/180)), 'blue')    

drawAxes()

main.bind("<KeyPress>", draw)
main.mainloop()