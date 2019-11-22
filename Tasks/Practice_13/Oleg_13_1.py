import tkinter
import random
import math

move_x = random.random()
move_y = math.sqrt(1 - move_x**2)

cSize = 800
n = 30

coords = [cSize//2, cSize//2]

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg = 'white', width = cSize, height = cSize)

circle = canvas.create_oval(cSize // 2 - n, cSize // 2 - n, cSize // 2 + n, cSize // 2 + n, fill = 'red')

def Draw():
    canvas.coords(circle, coords[0] - n, coords[1] - n, coords[0] + n, coords[1] + n)
    main.after(10, Draw)

def Move():
    global move_x
    global move_y
    
    coords[0] += move_x
    coords[1] += move_y
    
    if (coords[0] + n >= cSize or coords[0] - n <= 0):
        move_x = - move_x
    if (coords[1] + n >= cSize or coords[1] - n <= 0):
        move_y = - move_y
    
    main.after(2, Move)
    

canvas.pack()

Draw()
Move()

main.mainloop()



    