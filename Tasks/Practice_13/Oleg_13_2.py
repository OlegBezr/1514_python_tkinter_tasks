import tkinter
import random
from math import *
import time

cSize = 800
n = 200
s = 170
m = 150
h = 100
delta = 10

O = cSize//2

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = cSize, height = cSize)

circle = canvas.create_oval(O - n, O - n, O + n, O + n, fill = 'black', width = 3, outline = 'red')

for i in range(1, 13):
    canvas.create_text(O + (n-delta) * cos(2 * pi * (i + 9) / 12), O + (n-delta) * sin(2 * pi * (i + 9) / 12), text = str(i), fill = 'white')

seconds = canvas.create_line(O, O, O, O - s, width = 2, fill = 'blue')
minutes = canvas.create_line(O, O, O, O - m, width = 4, fill = 'green')
hours = canvas.create_line(O, O, O, O - h, width = 8, fill = 'white')

canvas.pack()

now = time.strftime("%H:%M:%S")

def ArrowSet(arrow, l, t, mult):
    canvas.coords(arrow, O, O, O + l * cos(2 * pi * (t/60 * mult - 1/4)), O + l * sin(2 * pi * (t/60 * mult - 1/4)))

def TimeSet():
    global label
    now_s = time.strftime("%S")
    now_m = time.strftime("%M")
    now_h = time.strftime("%H")
    label.config(text = now_h + ':' + now_m + ':' + now_s)
    ArrowSet(seconds, s, int(now_s), 1)
    ArrowSet(minutes, m, int(now_m), 1)
    ArrowSet(hours, h, int(now_h), 5)
    
    
    main.after(1000, TimeSet)
    
label = tkinter.Label(main, text = now)
label.pack()

TimeSet()
    
main.mainloop()