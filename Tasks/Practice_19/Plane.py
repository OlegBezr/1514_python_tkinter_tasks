import tkinter
import time
from math import *
sSize = [800, 800]
w = int(input("¬ведите ширину линий: "))
m = int(input("¬ведите длину шага: "))
numb = int(input("¬ведите номер формулы: "))
col = 'white'

formulas = [
 "100*cos(pi/180*sqrt(x*x + y*y))",
 "100*sin(pi/180*sqrt(x*x + y*y))",
 "2000*sin(sqrt(x*x + y*y))/sqrt(x*x+y*y)",
 "100*cos(0.01*x*y*pi/180)",
 "230*abs(cos(sqrt(x*x + y*y)*pi/180))/(sqrt(x*x + y*y)*0.01+1)",
 "sqrt(5*(500*500-x*x-y*y))-900"
]

a = [-0.25, -1, -0.25]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize[0], height = sSize[1])

def putpixel(x, y, color, wid):
    canvas.create_line(x - wid/2, y, x + wid/2, y, fill = color, width = wid)
    
def xs(x):
    return x + sSize[0]//2

def ys(y):
    return sSize[1]//2 - y

def Draw():    
    polygons = []
    for y1 in range(-250, 250, m):
        for x1 in range(-250, 250, m):
            add = []
            for ch in [[0, 0], [m, 0], [m, m], [0, m]]:
                x = x1 + ch[0]
                y = y1 + ch[1]
                z = eval(formulas[numb])
                x_real = x - a[0]/a[1] * y
                y_real = z - a[2]/a[1] * y
                add.append([x_real, y_real])
            
            polygons.append(add)
    
    for i in polygons:
        canvas.create_polygon(xs(i[0][0]), ys(i[0][1]), xs(i[1][0]), ys(i[1][1]), xs(i[2][0]), ys(i[2][1]), xs(i[3][0]), ys(i[3][1]), outline = 'white', fill = 'black', width = 1)  
        
    '''for y in range(-250, 255, +m):
        for x in range(-250, 255, +m):
            z = eval(formulas[numb])
            x_real = x - a[0]/a[1] * y
            y_real = z - a[2]/a[1] * y
            putpixel(xs(x_real), ys(y_real), 'green', 2)'''

Draw()
canvas.pack()
main.mainloop()