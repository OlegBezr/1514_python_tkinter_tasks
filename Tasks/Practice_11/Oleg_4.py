import tkinter
from math import *
CANVAS_SIZE = 600
n = int(input("Input nodes count: "))
r = int(input("Input circle radius: "))
# nodes - это вершины правильного n-угольника
nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * i / n),
CANVAS_SIZE // 2 + r * sin(2 * pi * i / n))
for i in range(n)]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white',
width = CANVAS_SIZE,
height = CANVAS_SIZE)

count = len(nodes)

for i in range(count):
    canvas.create_line(nodes[i], nodes[(i + (n - 1)//4 + 1) % count], width = 3, fill = 'red')

canvas.pack()
main.mainloop()