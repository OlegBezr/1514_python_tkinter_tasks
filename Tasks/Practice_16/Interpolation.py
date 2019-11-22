import tkinter
from math import *
sSize = [800, 600]
w = int(input("Введите ширину линий: "))
col = 'white'

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize[0], height = sSize[1])

dotes = list()
count = 0

def xs(x):
    return x + sSize[0]//2

def ys(y):
    return sSize[1]//2 - y

def xu(x):
    return x - sSize[0]//2

def yu(y):
    return -y + sSize[1]//2

def putpixel(x, y, color, wid):
    canvas.create_line(x - wid/2, y, x + wid/2, y, fill = color, width = wid)
    
def l(x, index):
    res = 1
    for i in range(count):
        if (i != index):
            res *= (x - dotes[i][0]) / (dotes[index][0] - dotes[i][0])
    return res 

def L(x):
    res = 0
    for i in range(count):
        res += l(x, i) * dotes[i][1]
    return res

def BuildGraphic():
    canvas.delete('all')
    
    for i in range(-sSize[0]//2, sSize[0]//2):
        putpixel(xs(i), ys(L(i)), col, w)
        canvas.create_line(xs(i), ys(L(i)), xs(i + 1), ys(L(i + 1)), fill = col, width = w)
        
    for i in dotes:
        putpixel(xs(i[0]), ys(i[1]), 'green', w + 5)    

def AddNode(event):
    global dotes, count
    for i in dotes:
        if(xu(event.x) == i[0]):
            print('Точка с данной координатой Х уже задана!')
            return 
        
    dotes.append([xu(event.x), yu(event.y)])
    dotes.sort()
    count = len(dotes)
    BuildGraphic()
    
def DeleteNode(event):
    global dotes, count
    for i in range(count):
        if(abs(dotes[i][0] - xu(event.x)) <= 5 and abs(dotes[i][1] - yu(event.y)) <= 5):
            dotes.pop(i)
            break
    count = len(dotes)
    BuildGraphic()
    
def GetInput(event):
    #print(event.num)
    if(event.num == 1):
        AddNode(event)
    elif(event.num == 3):
        DeleteNode(event)
    
canvas.bind('<Button>', GetInput)

canvas.pack()
main.mainloop()