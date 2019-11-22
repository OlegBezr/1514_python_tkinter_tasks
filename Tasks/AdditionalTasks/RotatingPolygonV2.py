import tkinter
from math import *
CANVAS_SIZE = 800
n = int(input("Input nodes count: "))
r = int(input("Input circle radius: "))

#вокруг какой вершины вращаю многоугольник
center = 0

#на сколько градусов за 1 раз вращается многоугольник
alpha = int(input("Input rotation angle: "))
#перевожу угол в радианы
angle = alpha / 180 * pi

# nodes - это вершины правильного n-угольника
nodes = [(CANVAS_SIZE // 2 + r * cos(2 * pi * i / n) - r,
CANVAS_SIZE // 2 + r * sin(2 * pi * i / n))
for i in range(n)]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = CANVAS_SIZE, height = CANVAS_SIZE)

#кол-во вершин многоугольника
count = len(nodes)

canvas.create_polygon(*nodes, width = 3, outline = 'red', fill = 'white')

def RotateSegment(dote1, dote2, angle):
    return [dote1[0] + (dote2[0] - dote1[0]) * cos(angle) + (dote1[1] - dote2[1]) * sin(angle),
            dote1[1] + (dote2[0] - dote1[0]) * sin(angle) + (dote2[1] - dote1[1]) * cos(angle)]    

def Rotate():
    #отчищаю холст
    canvas.delete('all')
    
    for i in range(count):
        #поворачиваю точку вокруг другой на угол angle
        nodes[i] = RotateSegment(nodes[center], nodes[i], angle)
    
    #отрисовываю линии многоугольника
    canvas.create_polygon(*nodes, width = 3, outline = 'red', fill = 'white')
    
    main.after(100, Rotate)

Rotate()

canvas.pack()
main.mainloop()