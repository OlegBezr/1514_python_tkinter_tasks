import tkinter
from math import *
CANVAS_SIZE = 800
n = int(input("Input nodes count: "))
r = int(input("Input circle radius: "))

# nodes - это вершины правильного n-угольника
nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * i / n),
          CANVAS_SIZE // 2 + r * sin(2 * pi * i / n))
          for i in range(n)]

#вокруг чего буду вращать многоугольник
center = [CANVAS_SIZE // 2, CANVAS_SIZE // 2]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = CANVAS_SIZE, height = CANVAS_SIZE)

count = len(nodes)
canvas.create_polygon(*nodes, width = 3, outline = 'red', fill = 'white')
    
#угол поворота
alpha = 3
#перевод в радианы
alpha = alpha / 180 * pi

#вращение отрезка относительно одного конца (dote1) 
def RotateSegment(dote1, dote2, angle):
    return [dote1[0] + (dote2[0] - dote1[0]) * cos(angle) + (dote1[1] - dote2[1]) * sin(angle),
            dote1[1] + (dote2[0] - dote1[0]) * sin(angle) + (dote2[1] - dote1[1]) * cos(angle)]    

def Rotate():
    global nodes
    #отчищаю холст
    canvas.delete('all')
    
    #создаю занового вершины многоугольника с поворотом
    nodes = [RotateSegment(center, nodes[i], alpha) for i in range(n)]    
    
    #отрисовываю линии многоугольника
    canvas.create_polygon(*nodes, width = 3, outline = 'red', fill = 'white')
    
    main.after(100, Rotate)

Rotate()

canvas.pack()
main.mainloop()