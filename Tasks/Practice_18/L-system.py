import tkinter
from math import *
sSize = [800, 600]
w = int(input("¬ведите ширину линий: "))
col = 'white'

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize[0], height = sSize[1])

def putpixel(x, y, color, wid):
    canvas.create_line(x - wid/2, y, x + wid/2, y, fill = color, width = wid)
    
def xs(x):
    return x + sSize[0]//2

def ys(y):
    return sSize[1]//2 - y

def xu(x):
    return x - sSize[0]//2

def yu(y):
    return -y + sSize[1]//2    

def RotateSegment(dote1, dote2, angle):
    return [dote1[0] + (dote2[0] - dote1[0]) * cos(angle) + (dote1[1] - dote2[1]) * sin(angle),
            dote1[1] + (dote2[0] - dote1[0]) * sin(angle) + (dote2[1] - dote1[1]) * cos(angle)]  

def AngleToRad(a):
    return (a / 180 * pi)


f = open('L.txt', 'r')
changes = {}
name = f.readline()
rot = int(f.readline())
stage = int(f.readline())
place = list(map(int, f.readline().split()))
move = int(f.readline())
state = f.readline()
for line in f:
    changes[line[0]] = line[2::]
    
print(name[0:-1], end = '; ')
print(rot, end = '; ')
print(state)

rot = AngleToRad(360 / rot)

'''stage = int(input("¬ведите этап эволюции: "))
place = list(map(int, input("¬ведите изначальные координаты: ").split()))
move = int(input("¬ведите длину базового отрезка: "))'''
place = [xs(place[0]), ys(place[1])]
savedPlace = place
angle = 0

for i in range(stage):
    state1 = ''
    for j in state:
        if j in changes:
            state1 += changes[j]
        else:
            state1 += j
    state = state1
print(state)

for i in state:
    if (i == 'F'):
        newPlace = [place[0] + move, place[1]]
        newPlace = RotateSegment(place, newPlace, angle)
        canvas.create_line(place, newPlace, fill = col, width = w)
        place = newPlace
    elif (i == 'f'):
        newPlace = [place[0] + move, place[1]]
        newPlace = RotateSegment(place, newPlace, angle)  
        place = newPlace
    elif (i == '+'):
        angle += rot
    elif (i == '-'):
        angle -= rot
    elif (i == '['):
        savedPlace = place
    elif (i == ']'):
        place = savedPlace
    elif (i == '|'):
        angle += pi
        
canvas.pack()
main.mainloop()