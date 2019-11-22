import tkinter
from math import *
import random
x, y = map(int, input("¬ведите размеры экрана:").split())
w = int(input("¬ведите толщину линий:"))

sSize = [x, y]
main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize[0], height = sSize[1])
canvas.pack()

center = [sSize[0]/2, sSize[1]/2]

a = int(input("¬ведите константу:"))

Q_abs = 100

def xs(x):
    return center[0] + x

def ys(y):
    return center[1] - y

def AngleToRad(a):
    return (a / 180 * pi)

def FromPolToDec(r, rad):
    return [r * cos(rad),  r * sin(rad)]

def putpixel(x, y, color):
    canvas.create_line((x, y), (x+1, y), fill=color, width = w)
    
def RandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)   
    return "#%02x%02x%02x" % (r, g, b) 

def GetCoordsAndDraw(r, rad):
    place = FromPolToDec(r, rad)
    putpixel(xs(place[0]), ys(place[1]), 'white')    

def PhermsCurve(rad):
    return sqrt(a * a * rad)
    
def Cartoida(rad):
    return 2 * a * (1 - cos(rad))

def Bernulli(rad):
    if (cos(rad * 2) > 0):
        return sqrt(cos(rad * 2) * a * a * 2)
    else:
        return 0
    
#k = random.randint(-10000, 10000)
k = 180 / pi * 50
def Roses(rad, k):
    return a * sin(k * rad)

par_a = 100
par_b = 60

def Paskal(rad):
    x = par_a * cos(rad) * cos(rad) + par_b * cos(rad)
    y = 0.5 * par_a * sin(2 * rad) + par_b * sin(rad)
    return [x, y]

def Draw():
    global alpha
    alpha += 1
    #alpha %= 360
    #radius = PhermsCurve(AngleToRad(alpha))
    #radius = Cartoida(AngleToRad(alpha))
    #radius = Bernulli(AngleToRad(alpha))
    #radius = Roses(AngleToRad(alpha), k)
    #GetCoordsAndDraw(radius, AngleToRad(alpha))
    
    place = Paskal(alpha)
    putpixel(xs(place[0]), ys(place[1]), 'white')
    main.after(1, Draw)

alpha = 0
Draw()
main.mainloop()