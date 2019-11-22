import tkinter
from math import *
sSize = [800, 600]
w = int(input("¬ведите ширину линий: "))
col = 'white'

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize[0], height = sSize[1])

dotes = list()
count = 0

smaller = 0.9
bigger = 1.1

center = [0, 0]

alpha = 0.1

def putpixel(x, y, color, wid):
    canvas.create_line(x - wid/2, y, x + wid/2, y, fill = color, width = wid)

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
    for i in range(count):
        if(abs(dotes[i][0] - event.x) <= 5 and abs(dotes[i][1] - event.y) <= 5):
            dotes.pop(i)
            break
    count = len(dotes)
    ConnectNodes()
    
def SetCenter(event):
    center[0] = event.x
    center[1] = event.y
    
def ChangeCoords(x1, x2, typ):
    if (typ == 0):
        return x1 + (x2 - x1) * bigger
    else:
        return x1 + (x2 - x1) * smaller

def ChangeNodes(dote1, dote2, typ):
    return [ChangeCoords(dote1[0], dote2[0], typ), ChangeCoords(dote1[1], dote2[1], typ)]

def Scale(typ):
    global dotes
    dotes1 = []
    for j in range(count):
        dotes1.append(ChangeNodes(center, dotes[j], typ))      
    dotes = dotes1
    ConnectNodes()
    
def RotateSegment(dote1, dote2, angle):
    return [dote1[0] + (dote2[0] - dote1[0]) * cos(angle) + (dote1[1] - dote2[1]) * sin(angle),
            dote1[1] + (dote2[0] - dote1[0]) * sin(angle) + (dote2[1] - dote1[1]) * cos(angle)]    

def RotateSegmentUpDown(dote1, dote2, typ):
    if (typ == 0):
        return RotateSegment(dote1, dote2, alpha)
    elif (typ == 1):
        return RotateSegment(dote1, dote2, -alpha)
    
    
def Rotate(typ):
    global dotes
    dotes1 = []
    for j in range(count):
        dotes1.append(RotateSegmentUpDown(center, dotes[j], typ))      
    dotes = dotes1
    ConnectNodes()
    
def OperatePolygon(key):
    typ = key.keycode
    if (typ == 38 or typ == 87):
        Rotate(0)
    elif (typ == 40 or typ == 83):
        Rotate(1)
    elif (typ == 37 or typ == 65):
        Scale(1)
    elif (typ == 39 or typ == 68):
        Scale(0)
    putpixel(center[0], center[1], 'green', w + 2)
    
def GetInput(event):
    print(event.num)
    if(event.num == 1):
        AddNode(event)
    elif(event.num == 3):
        DeleteNode(event)
    elif(event.num == 2):
        SetCenter(event)
    putpixel(center[0], center[1], 'green', w + 2)
    
canvas.bind('<Button>', GetInput)
main.bind('<KeyPress>', OperatePolygon)

canvas.pack()
main.mainloop()