import tkinter
import time
from math import *
CANVAS_SIZE = 800
n = int(input("Input nodes count: "))
r = int(input("Input circle radius: "))
k = float(input("Input k: "))
rep = int(input("Number of times: "))

# nodes - это вершины правильного n-угольника
nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * i / n),
CANVAS_SIZE // 2 + r * sin(2 * pi * i / n))
for i in range(n)]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = CANVAS_SIZE, height = CANVAS_SIZE)
canvas.pack()

def DrawPolygon():
    for i in range(n):
        canvas.create_line(nodes[i], nodes[(i + 1) % n], width = 3, fill = 'red')
    
def ChangeCoords(x1, x2):
    return x1 + (x2 - x1) / (k + 1) * k

def ChangeNodes(dote1, dote2):
    return [ChangeCoords(dote1[0], dote2[0]), ChangeCoords(dote1[1], dote2[1])]

DrawPolygon()

for i in range(rep - 1):
    nodes1 = []
    for j in range(n):
        nodes1.append(ChangeNodes(nodes[j], nodes[(j + 1) % n]))
    nodes = nodes1
    DrawPolygon()
    #time.sleep(0.1)

main.mainloop()
    



                