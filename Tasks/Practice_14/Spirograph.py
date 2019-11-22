import tkinter
import random
from math import *
import time

sSize = 800
n = 200

A = int(input("Введите радиус большей окружности: "))
B = int(input("Введите радиус меньшей окружности: "))    
D = int(input("Введите радиус дырки спирографа: "))
w = int(input("Введите ширину: "))

startInner = [(A - B) * cos(0) + D * cos(0), (A - B) * sin(0) + D * sin(0)]
startOuter = [(A + B) * cos(0) + D * cos(-pi), (A + B) * sin(0) + D * sin(-pi)]

color = 'white'
                        
copy_t = 0
t = 0

O = sSize//2

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'black', width = sSize, height = sSize)
canvas.pack()

def xs(x):
    return sSize//2 + x
def ys(y):
    return sSize//2 - y

def putpixel(x, y, color):
    canvas.create_line((x, y), (x+1, y), fill=color, width = w)
    
def RandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return "#%02x%02x%02x" % (r, g, b)    

def DrawInnerSpirograph():
    global t
    global copy_t
    global color
    copy_t += 10
    t = copy_t / 1000
    place_x = (A - B) * cos(-t) + D * cos(t * A / B - t)
    place_y = (A - B) * sin(-t) + D * sin(t * A / B - t)
    
    if(copy_t % 37 == 0):
        color = RandomColor()
        
    if ((-t * 1000) % 6280 <= 5 and (t * (A - B) * 1000) % 6280 <= 5):
        canvas.create_text(O, O, text = 'Спирограф нарисован успешно!', fill = color)
        print(2)
        return 0
    elif (abs(place_x - startInner[0]) < 0.1 and abs(place_y - startInner[1]) < 0.1):
        canvas.create_text(O, O, text = 'Спирограф нарисован успешно!', fill = color)
        print(1)
        return 0
        
    putpixel(xs(place_x), ys(place_y), color)
    
    main.after(1, DrawInnerSpirograph)

def DrawOuterSpirograph():
    global t
    global copy_t
    global color
    copy_t += 10
    t = copy_t / 1000
    place_x = (A + B) * cos(t) + D * cos(t * A / B + t - pi)
    place_y = (A + B) * sin(t) + D * sin(t * A / B + t - pi)
    
    if(copy_t % 37 == 0):
        color = RandomColor()    
    
    if ((t * 1000) % 6280 <= 5 and (t * (A + B) * 1000) % 6280 <= 5):
        canvas.create_text(O, O, text = 'Спирограф нарисован успешно!', fill = color)
        print(2)
        return 0    
    elif (abs(place_x - startOuter[0]) < 0.3 and abs(place_y - startOuter[1]) < 0.3):
        canvas.create_text(O, O, text = 'Спирограф нарисован успешно!', fill = color)
        print(1)
        return 0
    
    putpixel(xs(place_x), ys(place_y), color) 
    
    main.after(1, DrawOuterSpirograph)
    

#DrawInnerSpirograph()
DrawOuterSpirograph()

main.mainloop()