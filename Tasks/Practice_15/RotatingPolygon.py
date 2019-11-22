import tkinter
from math import *
CANVAS_SIZE = 800
n = int(input("Input nodes count: "))
r = int(input("Input circle radius: "))

# nodes - это вершины правильного n-угольника
nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * i / n),
CANVAS_SIZE // 2 + r * sin(2 * pi * i / n))
for i in range(n)]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = CANVAS_SIZE, height = CANVAS_SIZE)

count = len(nodes)

for i in range(count):
    canvas.create_line(nodes[i], nodes[(i + 1) % count], width = 3, fill = 'red')
    
alpha = 0

def Rotate():
    global alpha
    alpha += 0.02
    #отчищаю холст
    canvas.delete('all')
    
    #создаю занового вершины многоугольника с поворотом
    nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * (i / n + alpha)), CANVAS_SIZE // 2 + r * sin(2 * pi * (i / n + alpha))) for i in range(n)]    
    
    #отрисовываю линии многоугольника
    for i in range(count):
        canvas.create_line(nodes[i], nodes[(i + 1) % count], width = 3, fill = 'red')    
    
    main.after(100, Rotate)

Rotate()

canvas.pack()
main.mainloop()