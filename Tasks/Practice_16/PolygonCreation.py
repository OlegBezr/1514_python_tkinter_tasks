import tkinter
from math import *
sSize = [800, 600]
w = int(input("¬ведите ширину линий: "))
col = 'white'

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize[0], height = sSize[1])

dotes = list()
count = 0

def putpixel(x, y, color, wid):
    canvas.create_line(x, y, x + 1, y, fill = color, width = wid)

def ConnectNodes():
    canvas.delete('all')
    for i in range(count):
        putpixel(dotes[i][0], dotes[i][1], col, w + 2)
        
        canvas.create_line(dotes[i], dotes[(i + 1) % count], fill = col, width = w)

def AddNode(event):
    global dotes, count
    dotes.append([event.x, event.y])
    dotes.sort()
    count = len(dotes)
    ConnectNodes()
    
def DeleteNode(event):
    global dotes, count
    #for i in range(count):
        #if(abs(dotes[i][0] - event.x) <= 5 and abs(dotes[i][1] - event.y) <= 5):
            #dotes.pop(i)
            #break
    if (len(dotes) > 0):
        dotes.pop()
    count = len(dotes)
    ConnectNodes()
    
def GetInput(event):
    print(event.num)
    if(event.num == 1):
        AddNode(event)
    elif(event.num == 3):
        DeleteNode(event)
    
canvas.bind('<Button>', GetInput)

canvas.pack()
main.mainloop()